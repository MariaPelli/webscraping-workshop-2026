"""Offline-Vertragstests für die in den Demos sichtbaren Parser und API-Fehler.

Start im Repo: python -m unittest discover -s tests -p test_api_examples.py -v
Die Tests extrahieren nur Funktionsdefinitionen; keine Notebook-Live-Aufrufe.
"""
import ast
from copy import deepcopy
from datetime import date, datetime, timezone
import json
import math
from numbers import Real
from pathlib import Path
import traceback
import unittest
from unittest.mock import MagicMock, patch

import nbformat
import pandas as pd
import requests
from lxml import etree

ROOT = Path(__file__).resolve().parents[1]


def load_functions(filename):
    namespace = {
        "pd": pd, "requests": requests, "etree": etree, "math": math,
        "date": date, "datetime": datetime, "timezone": timezone, "Real": Real,
        "ROOT": ROOT, "json": json,
    }
    notebook = nbformat.read(ROOT / "demos" / filename, as_version=4)
    for cell in notebook.cells:
        if cell.cell_type != "code":
            continue
        tree = ast.parse(cell.source)
        definitions = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
        if definitions:
            module = ast.Module(body=definitions, type_ignores=[])
            exec(compile(module, filename, "exec"), namespace)
    return namespace


class APIExampleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ezb = load_functions("01_strukturierte_daten_ezb.ipynb")
        cls.api = load_functions("02_rest_apis_coingecko_flickr.ipynb")
        cls.xml = (ROOT / "data/samples/ezb_sample.xml").read_bytes()
        cls.coin = json.loads((ROOT / "data/samples/coingecko_sample.json").read_text())["payload"]
        cls.flickr = json.loads((ROOT / "data/samples/flickr_sample.json").read_text())["payload"]

    def test_ezb_units_and_date(self):
        rates = self.ezb["parse_ezb"](self.xml)
        self.assertEqual(len(rates), 4)
        self.assertEqual(set(rates.rate_date), {"2026-09-01"})
        self.assertAlmostEqual(rates.set_index("currency").loc["CHF", "rate_per_eur"], .96)
        self.assertEqual(set(rates.base_currency), {"EUR"})

    def test_ezb_wrong_namespace_does_not_silently_return_empty(self):
        bad = self.xml.replace(b"http://www.ecb.int/vocabulary/2002-08-01/eurofxref", b"urn:changed")
        with self.assertRaisesRegex(ValueError, "Datumsblock"):
            self.ezb["parse_ezb"](bad)

    def test_ezb_duplicate_and_nonfinite_rates_fail(self):
        for bad in (self.xml.replace(b'currency="USD"', b'currency="CHF"'),
                    self.xml.replace(b'rate="0.9600"', b'rate="NaN"')):
            with self.assertRaises(ValueError):
                self.ezb["parse_ezb"](bad)

    def test_coin_grain_and_timestamp(self):
        frame = self.api["parse_coingecko"](self.coin, ("bitcoin", "ethereum"), ("eur", "chf"))
        self.assertEqual(len(frame), 4)
        self.assertFalse(frame.duplicated(["coin_id", "quote_currency"]).any())
        self.assertEqual(set(frame.provider_updated_at_utc), {"2026-09-01T08:00:00+00:00"})

    def test_coin_missing_null_and_boolean_are_not_prices(self):
        for price in (None, True, float("nan")):
            bad = deepcopy(self.coin)
            bad["bitcoin"]["eur"] = price
            with self.assertRaisesRegex(ValueError, "Preis"):
                self.api["parse_coingecko"](bad, ("bitcoin",), ("eur",))
        with self.assertRaisesRegex(ValueError, "Coin-ID"):
            self.api["parse_coingecko"]({}, ("bitcoin",), ("eur",))

    def test_flickr_api_failure_is_not_http_success(self):
        with self.assertRaisesRegex(ValueError, "API-Status"):
            self.api["parse_flickr"]({"stat": "fail", "code": 100, "message": "Invalid API key"})

    def test_flickr_schema_pagination_and_duplicates(self):
        frame, total = self.api["parse_flickr"](self.flickr)
        self.assertEqual((len(frame), total), (3, 3))
        for change in ("duplicate", "page", "missing_license"):
            bad = deepcopy(self.flickr)
            if change == "duplicate":
                bad["photos"]["photo"][1]["id"] = bad["photos"]["photo"][0]["id"]
            elif change == "page":
                bad["photos"]["page"] = 2
            else:
                del bad["photos"]["photo"][0]["license"]
            with self.assertRaises(ValueError):
                self.api["parse_flickr"](bad)

    def test_flickr_legitimate_empty_search_has_columns(self):
        empty = {"stat": "ok", "photos": {"page": 1, "total": "0", "photo": []}}
        frame, total = self.api["parse_flickr"](empty)
        self.assertTrue(frame.empty)
        self.assertIn("photo_id", frame.columns)
        self.assertEqual(total, 0)

    def test_network_exception_does_not_expose_key(self):
        marker = "SYNTHETIC_TEST_CREDENTIAL"
        with patch("requests.get", side_effect=requests.ConnectionError("?api_key=" + marker)):
            try:
                self.api["fetch_json"]("https://example.invalid/", provider="Flickr", params={"api_key": marker})
            except RuntimeError as error:
                rendered = "".join(traceback.format_exception(error))
                self.assertNotIn(marker, rendered)
                self.assertIn("Netzwerkfehler", rendered)
            else:
                self.fail("Network error was not raised")

    def test_user_agent_keeps_provider_authentication_header(self):
        response = MagicMock()
        response.status_code = 200
        response.__enter__.return_value = response
        response.json.return_value = {"example": "ok"}
        with patch("requests.get", return_value=response) as mocked:
            self.api["fetch_json"](
                "https://example.invalid/", provider="CoinGecko", params={},
                headers={"x-cg-demo-api-key": "SYNTHETIC_TEST_CREDENTIAL"},
            )
        headers = mocked.call_args.kwargs["headers"]
        self.assertEqual(headers["User-Agent"], "WebscrapingWorkshop/0.2 (educational exercise)")
        self.assertEqual(headers["x-cg-demo-api-key"], "SYNTHETIC_TEST_CREDENTIAL")

    def test_http_and_bad_json_errors_are_sanitized(self):
        marker = "SYNTHETIC_TEST_CREDENTIAL"
        for status in (401, 429, 503, 200):
            response = MagicMock()
            response.status_code = status
            response.__enter__.return_value = response
            response.json.side_effect = ValueError("raw response " + marker)
            with patch("requests.get", return_value=response) as mocked:
                try:
                    self.api["fetch_json"]("https://example.invalid/", provider="Flickr", params={"api_key": marker})
                except (RuntimeError, ValueError) as error:
                    self.assertNotIn(marker, "".join(traceback.format_exception(error)))
                    self.assertFalse(mocked.call_args.kwargs["allow_redirects"])
                    self.assertEqual(mocked.call_args.kwargs["timeout"], (5, 20))
                else:
                    self.fail("HTTP/JSON error was not raised")


if __name__ == "__main__":
    unittest.main()
