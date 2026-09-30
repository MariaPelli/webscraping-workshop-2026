"""Gemeinsamer Einrichtungstest für CLI und Notebook.

Der Standardtest verwendet nur synthetische Dateien, einen kurzlebigen lokalen
HTTP-Server und den konfigurierten Selenium-Dienst. Es gibt keinen Ersatz für
eine fehlgeschlagene Browserprüfung. Live-Abrufe sind separat zuschaltbar.
"""

from __future__ import annotations

import importlib
import importlib.metadata
import json
import os
import platform
import sys
import threading
import time
from contextlib import contextmanager
from datetime import datetime, timezone
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Callable, Iterator
from urllib.parse import quote, urlsplit


PACKAGES = {
    "requests": "requests",
    "bs4": "beautifulsoup4",
    "lxml": "lxml",
    "pandas": "pandas",
    "selenium": "selenium",
    "dotenv": "python-dotenv",
    "ipykernel": "ipykernel",
    "jupyterlab": "jupyterlab",
    "matplotlib": "matplotlib",
    "nbformat": "nbformat",
    "nbclient": "nbclient",
}


class SetupCheckError(Exception):
    """Fehlertext ohne vertrauliche Verbindungs- oder Umgebungsinformationen."""


def find_repo_root(start: Path | str | None = None) -> Path:
    """Repo relativ zu cwd/Notebook finden, ohne einen persönlichen Pfad zu setzen."""
    location = Path(start if start is not None else Path.cwd()).resolve()
    if location.is_file():
        location = location.parent
    for candidate in (location, *location.parents):
        if (
            (candidate / "src/webscraping_workshop/checks.py").is_file()
            and (candidate / "data/fixtures/synthetic_records.json").is_file()
        ):
            return candidate
    raise SetupCheckError(
        "Repo-Wurzel nicht gefunden. Öffne Terminal/Notebook innerhalb des entpackten Repos."
    )


def resolve_browser_url(repo_root: Path) -> str:
    """Explizite Prozessumgebung hat Vorrang vor .env, z.B. in Codespaces."""
    from dotenv import load_dotenv

    load_dotenv(repo_root / ".env", override=False)
    configured = os.getenv("SELENIUM_REMOTE_URL", "").strip()
    if configured:
        parsed = urlsplit(configured)
        try:
            port = parsed.port
        except ValueError as exc:
            raise SetupCheckError("SELENIUM_REMOTE_URL enthält einen ungültigen Port.") from exc
        if (
            parsed.scheme not in {"http", "https"}
            or not parsed.hostname
            or parsed.username is not None
            or parsed.password is not None
            or parsed.query
            or parsed.fragment
            or (port is not None and not 1 <= port <= 65535)
        ):
            raise SetupCheckError(
                "SELENIUM_REMOTE_URL muss eine HTTP(S)-Adresse ohne Zugangsdaten, Query oder Fragment sein."
            )
        return configured.rstrip("/")
    raw_port = os.getenv("SELENIUM_PORT", "4444").strip()
    try:
        port = int(raw_port)
    except ValueError as exc:
        raise SetupCheckError("SELENIUM_PORT muss eine ganze Zahl zwischen 1 und 65535 sein.") from exc
    if not 1 <= port <= 65535:
        raise SetupCheckError("SELENIUM_PORT muss zwischen 1 und 65535 liegen.")
    return f"http://127.0.0.1:{port}"


class _QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: Any) -> None:
        pass


@contextmanager
def fixture_server(directory: Path) -> Iterator[str]:
    """Freien Loopback-Port verwenden; Server und Thread danach immer beenden."""
    handler = partial(_QuietHandler, directory=str(directory))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    server.daemon_threads = True
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


def parse_catalog_html(html: str) -> list[dict[str, Any]]:
    """Drei synthetische Datensätze aus dem statischen oder gerenderten DOM lesen."""
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "lxml")
    table = soup.select_one("table#catalog[data-synthetic='true']")
    if table is None:
        raise SetupCheckError("Die erwartete synthetische HTML-Tabelle fehlt.")
    records = []
    for row in table.select("tbody tr"):
        cells = [row.select_one(f".{name}") for name in ("id", "title", "price")]
        if any(cell is None for cell in cells):
            raise SetupCheckError("Eine HTML-Zeile hat nicht alle erwarteten Felder.")
        try:
            record = {
                "id": int(cells[0].get_text(strip=True)),
                "title": cells[1].get_text(strip=True),
                "price_chf": float(cells[2].get_text(strip=True)),
            }
        except ValueError as exc:
            raise SetupCheckError("ID oder Preis einer HTML-Zeile ist ungültig.") from exc
        if not record["title"]:
            raise SetupCheckError("Ein Buchtitel fehlt.")
        records.append(record)
    if len(records) != 3 or len({row["id"] for row in records}) != 3:
        raise SetupCheckError("Erwartet werden genau 3 Datensätze mit eindeutigen IDs.")
    return records


def _expected_records(root: Path) -> list[dict[str, Any]]:
    payload = json.loads((root / "data/fixtures/synthetic_records.json").read_text(encoding="utf-8"))
    if payload.get("synthetic") is not True or len(payload.get("records", [])) != 3:
        raise SetupCheckError("Die synthetische JSON-Vergleichsdatei ist unvollständig.")
    return payload["records"]


def _http_and_csv(root: Path) -> str:
    import pandas as pd
    import requests

    expected = _expected_records(root)
    # Loopback-Abfragen dürfen nicht versehentlich über einen Firmenproxy laufen.
    with requests.Session() as session:
        session.trust_env = False
        with fixture_server(root / "data/fixtures") as base:
            response = session.get(f"{base}/synthetic_records.json", timeout=(3, 5))
            response.raise_for_status()
            payload = response.json()
            if payload.get("synthetic") is not True or payload.get("records") != expected:
                raise SetupCheckError("Der JSON-HTTP-Abruf stimmt nicht mit den Testdaten überein.")
            response = session.get(f"{base}/static_catalog.html", timeout=(3, 5))
            response.raise_for_status()
            response.encoding = "utf-8"
            parsed = parse_catalog_html(response.text)
            if parsed != expected:
                raise SetupCheckError("HTML- und JSON-Datensätze stimmen nicht überein.")
    frame = pd.DataFrame(parsed, columns=["id", "title", "price_chf"])
    output = root / "data/output/setup_records.csv"
    output.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output, index=False, encoding="utf-8")
    loaded = pd.read_csv(output, encoding="utf-8")
    pd.testing.assert_frame_equal(frame, loaded)
    return "JSON und HTML per lokalem HTTP abgerufen; 3 gleiche Datensätze; CSV gespeichert und zurückgelesen."


def _wait_for_selenium(remote_url: str, timeout: float = 45.0) -> None:
    import requests

    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        remaining = deadline - time.monotonic()
        try:
            with requests.Session() as session:
                session.trust_env = False
                response = session.get(remote_url + "/status", timeout=max(0.1, min(3.0, remaining / 2)))
                response.raise_for_status()
                if response.json().get("value", {}).get("ready") is True:
                    return
        except (requests.RequestException, ValueError, AttributeError):
            pass
        remaining = deadline - time.monotonic()
        if remaining > 0:
            time.sleep(min(1.0, remaining))
    raise SetupCheckError(
        "Selenium ist nach maximal 45 Sekunden nicht bereit. Prüfe den gestarteten Docker-/Codespaces-Dienst "
        "und seine Logs. Lokal: docker compose up -d. Danach erneut ausführen."
    )


def _browser_check(root: Path) -> str:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.remote.client_config import ClientConfig
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from selenium.webdriver.support.ui import WebDriverWait

    remote_url = resolve_browser_url(root)
    _wait_for_selenium(remote_url)
    html = (root / "data/fixtures/dynamic_catalog.html").read_text(encoding="utf-8")
    expected = _expected_records(root)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    driver = None
    failure = None
    try:
        # Begrenzte WebDriver-Kommandos; damit kann ein nicht reagierender Dienst
        # den Einrichtungstest nicht unbegrenzt blockieren.
        from selenium.webdriver.common.proxy import Proxy, ProxyType

        client_config = ClientConfig(
            remote_server_addr=remote_url,
            timeout=30,
            proxy=Proxy(raw={"proxyType": ProxyType.DIRECT}),
        )
        connection = RemoteConnection(client_config=client_config)
        driver = webdriver.Remote(command_executor=connection, options=options)
        driver.set_page_load_timeout(20)
        driver.get("data:text/html;charset=utf-8," + quote(html, safe=""))
        WebDriverWait(driver, 15).until(
            lambda current: len(current.find_elements(By.CSS_SELECTOR, "#catalog tbody tr")) == 3
        )
        records = parse_catalog_html(driver.page_source)
        if records != expected:
            raise SetupCheckError("Die 3 JavaScript-Datensätze stimmen nicht mit den Testdaten überein.")
    except Exception as exc:
        failure = exc
        raise
    finally:
        if driver is not None:
            try:
                driver.quit()
            except Exception as exc:
                if failure is None:
                    raise SetupCheckError(
                        "Browserinhalt geprüft, Sitzung aber nicht sauber beendet. Prüfe die Selenium-Logs."
                    ) from exc
    return "Echte Selenium-Remote-Sitzung: JavaScript erzeugt 3 korrekte Datensätze; Sitzung beendet."


def _online_probe(kind: str) -> str:
    import requests

    targets = {
        "ecb": "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml",
        "books": "https://books.toscrape.com/",
    }
    response = requests.get(
        targets[kind],
        headers={"User-Agent": "WebscrapingWorkshopSetup/0.1 (educational connectivity check)"},
        timeout=(5, 15),
    )
    response.raise_for_status()
    if not 200 <= response.status_code < 300:
        raise SetupCheckError(f"Unerwarteter HTTP-Status {response.status_code} beim Live-Abruf.")
    if kind == "ecb":
        from lxml import etree

        parser = etree.XMLParser(resolve_entities=False, no_network=True)
        document = etree.fromstring(response.content, parser=parser)
        if not document.xpath("//*[local-name()='Cube'][@currency][@rate]"):
            raise SetupCheckError("HTTP erfolgreich, aber erwartete ECB-Wechselkurse fehlen im XML.")
        return f"HTTP {response.status_code}; XML mit Wechselkursen erreicht (kein fachlicher Kurs-Task)."
    from bs4 import BeautifulSoup

    document = BeautifulSoup(response.content, "lxml")
    title = document.title.get_text() if document.title else ""
    if "Books to Scrape" not in title or not document.select("article.product_pod"):
        raise SetupCheckError("HTTP erfolgreich, aber der erwartete Buchkatalog fehlt im HTML.")
    return f"HTTP {response.status_code}; HTML mit Buchartikeln erreicht (kein vollständiger Scraping-Test)."


def _safe_error(exc: Exception) -> str:
    if isinstance(exc, SetupCheckError):
        return str(exc)
    # Drittpaket-Exceptions können URLs, Systempfade oder Proxy-Zugangsdaten
    # enthalten. Der Report speichert nur Typ, Statuscode und gezielte Hinweise.
    name = type(exc).__name__
    response = getattr(exc, "response", None)
    code = getattr(response, "status_code", None)
    suffix = f", HTTP {code}" if isinstance(code, int) else ""
    if name in {"SessionNotCreatedException", "WebDriverException", "TimeoutException", "MaxRetryError"}:
        hint = " Prüfe Selenium-Dienst, Container-Logs und laufende Browsersitzungen."
    elif name in {"ConnectionError", "ConnectTimeout", "ReadTimeout", "ProxyError", "SSLError"}:
        hint = " Prüfe Verbindung, Proxy und Zertifikate für die betreffende Prüfung."
    elif name in {"PermissionError", "OSError"}:
        hint = " Prüfe Dateien und Schreibrechte im Repo."
    else:
        hint = " Siehe docs/TROUBLESHOOTING.md; melde Prüfpunkt und Fehlertyp."
    return f"{name}{suffix}.{hint}"


def run_setup_checks(
    root: Path | str | None = None,
    *,
    include_browser: bool = True,
    online: bool = False,
    on_result: Callable[[dict[str, str]], None] | None = None,
) -> dict[str, Any]:
    """Alle Ergebnisse sammeln; Fehlschläge nie als bestandenen Test ausgeben."""
    results: list[dict[str, str]] = []

    def add(key: str, label: str, status: str, detail: str, group: str = "core") -> None:
        result = {"key": key, "label": label, "status": status, "detail": detail, "group": group}
        results.append(result)
        if on_result is not None:
            on_result(result)

    def perform(key: str, label: str, action: Callable[[], str], group: str = "core") -> bool:
        try:
            detail = action()
        except Exception as exc:
            add(key, label, "fail", _safe_error(exc), group)
            return False
        add(key, label, "pass", detail, group)
        return True

    correct_python = sys.version_info[:2] == (3, 12)
    add("python", "Python", "pass" if correct_python else "fail", f"Python {platform.python_version()}; vorgesehen ist Python 3.12.")
    versions = {}
    missing = []
    for module, package in PACKAGES.items():
        try:
            importlib.import_module(module)
            versions[package] = importlib.metadata.version(package)
        except Exception:
            missing.append(package)
    imports_ok = not missing
    add(
        "imports", "Python-Pakete", "pass" if imports_ok else "fail",
        "Alle benötigten Pakete importiert." if imports_ok else "Nicht importierbar: " + ", ".join(missing) + ". Wähle die Workshop-Umgebung und installiere requirements.txt.",
    )
    try:
        repo_root = find_repo_root(root)
        paths_ok = all((repo_root / f"data/fixtures/{name}").is_file() for name in (
            "synthetic_records.json", "static_catalog.html", "dynamic_catalog.html"
        ))
        if not paths_ok:
            raise SetupCheckError("Mindestens eine synthetische Fixture-Datei fehlt. Entpacke das vollständige Repo.")
        add("paths", "Relative Repo-Pfade", "pass", "Repo und alle 3 Fixture-Dateien gefunden; keine festen Benutzerpfade nötig.")
    except Exception as exc:
        repo_root = None
        add("paths", "Relative Repo-Pfade", "fail", _safe_error(exc))

    runnable = imports_ok and repo_root is not None
    if runnable:
        perform("http_csv", "HTTP, HTML/JSON und CSV", lambda: _http_and_csv(repo_root))
    else:
        add("http_csv", "HTTP, HTML/JSON und CSV", "skip", "Nicht ausgeführt, weil Pakete oder Repo-Dateien fehlen.")
    if not include_browser:
        add("browser", "Selenium und JavaScript", "skip", "Bewusst mit --skip-browser ausgelassen. Dies ist nur ein Teilergebnis.")
    elif runnable:
        perform("browser", "Selenium und JavaScript", lambda: _browser_check(repo_root))
    else:
        add("browser", "Selenium und JavaScript", "skip", "Nicht ausgeführt, weil Pakete oder Repo-Dateien fehlen.")
    if online:
        for key, label in (("ecb", "Live: ECB-XML"), ("books", "Live: Books to Scrape")):
            if imports_ok:
                perform("online_" + key, label, lambda key=key: _online_probe(key), group="online")
            else:
                add("online_" + key, label, "skip", "Nicht ausgeführt, weil benötigte Pakete fehlen.", group="online")

    core = [r for r in results if r["group"] == "core"]
    required = [r for r in core if include_browser or r["key"] != "browser"]
    core_status = "pass" if all(r["status"] == "pass" for r in required) else "fail"
    live = [r for r in results if r["group"] == "online"]
    online_status = ("pass" if all(r["status"] == "pass" for r in live) else "fail") if online else "not_run"
    return {
        "schema_version": 1,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "full" if include_browser else "partial_without_browser",
        "core_status": core_status,
        "online_status": online_status,
        "overall_status": "pass" if core_status == "pass" and online_status != "fail" else "fail",
        "python_version": platform.python_version(),
        "operating_system": platform.system(),
        "architecture": platform.machine(),
        "package_versions": versions,
        "checks": results,
    }


def format_result(result: dict[str, str]) -> str:
    marker = {"pass": "OK", "fail": "FEHLER", "skip": "AUSGELASSEN"}[result["status"]]
    return f"[{marker}] {result['label']}: {result['detail']}"


def summary_text(report: dict[str, Any]) -> str:
    partial = report["scope"] == "partial_without_browser"
    if report["core_status"] != "pass":
        base = "TEILTEST FEHLGESCHLAGEN" if partial else "SETUP FEHLGESCHLAGEN"
    elif partial:
        base = "TEILTEST OK – Browserprüfung ausgelassen; vollständige Einrichtung noch nicht bestätigt."
    elif report["online_status"] == "fail":
        base = "SETUP BASIS OK"
    else:
        base = "SETUP OK"
    if report["online_status"] == "pass":
        return base + " | LIVE-TEST OK"
    if report["online_status"] == "fail":
        return base + " | LIVE-TEST FEHLGESCHLAGEN"
    return base + " | Live-Erreichbarkeit nicht geprüft."


def write_report(report: dict[str, Any], destination: Path | str) -> Path:
    target = Path(destination)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return target
