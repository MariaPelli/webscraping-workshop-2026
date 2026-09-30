"""Kleine Regressionstests für Kernfunktion und aussagekräftige Fehlermeldungen.

Aus der Repo-Wurzel: python -m unittest discover -s tests -v
Diese Tests prüfen keine echte Browsersitzung; dafür dient verify_setup.py.
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from webscraping_workshop.checks import (
    SetupCheckError, find_repo_root, parse_catalog_html, resolve_browser_url,
    run_setup_checks, summary_text,
)


class SetupChecksTests(unittest.TestCase):
    def test_root_from_notebook_directory(self):
        self.assertEqual(find_repo_root(ROOT / "notebooks"), ROOT)

    def test_baseline_uses_real_local_http_and_csv(self):
        report = run_setup_checks(ROOT, include_browser=False)
        self.assertEqual(report["core_status"], "pass", report)
        self.assertEqual(report["scope"], "partial_without_browser")
        self.assertEqual(report["online_status"], "not_run")
        self.assertIn("TEILTEST OK", summary_text(report))
        self.assertNotIn("SETUP OK", summary_text(report))

    def test_unrendered_dynamic_html_is_not_false_success(self):
        html = (ROOT / "data/fixtures/dynamic_catalog.html").read_text(encoding="utf-8")
        with self.assertRaises(SetupCheckError):
            parse_catalog_html(html)

    def test_remote_environment_wins_over_dotenv(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / ".env").write_text("SELENIUM_REMOTE_URL=http://127.0.0.1:5555\n", encoding="utf-8")
            with patch.dict(os.environ, {"SELENIUM_REMOTE_URL": "http://selenium:4444"}, clear=True):
                self.assertEqual(resolve_browser_url(root), "http://selenium:4444")

    def test_invalid_port_and_credentials_rejected_without_echo(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {"SELENIUM_PORT": "70000"}, clear=True):
                with self.assertRaises(SetupCheckError):
                    resolve_browser_url(Path(folder))
            with patch.dict(os.environ, {"SELENIUM_REMOTE_URL": "http://user:privatevalue@host:4444"}, clear=True):
                with self.assertRaises(SetupCheckError) as result:
                    resolve_browser_url(Path(folder))
                self.assertNotIn("privatevalue", str(result.exception))

    def test_browser_failure_does_not_become_setup_ok(self):
        with patch("webscraping_workshop.checks._browser_check", side_effect=SetupCheckError("Testfehler")):
            report = run_setup_checks(ROOT)
        self.assertEqual(report["overall_status"], "fail")
        self.assertIn("SETUP FEHLGESCHLAGEN", summary_text(report))

    def test_requested_live_failure_is_separate_and_fails_overall(self):
        with patch("webscraping_workshop.checks._online_probe", side_effect=SetupCheckError("Live-Testfehler")):
            report = run_setup_checks(ROOT, include_browser=False, online=True)
        self.assertEqual(report["core_status"], "pass")
        self.assertEqual(report["online_status"], "fail")
        self.assertEqual(report["overall_status"], "fail")
        self.assertIn("LIVE-TEST FEHLGESCHLAGEN", summary_text(report))


if __name__ == "__main__":
    unittest.main()
