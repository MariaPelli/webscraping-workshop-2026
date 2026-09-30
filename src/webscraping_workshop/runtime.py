"""Browser-Verbindung für die Lernnotebooks; Extraktion bleibt im Notebook."""

from contextlib import contextmanager
from pathlib import Path
from urllib.parse import quote

from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.remote.client_config import ClientConfig
from selenium.webdriver.remote.remote_connection import RemoteConnection

from .checks import _wait_for_selenium, resolve_browser_url


def html_data_url(html: str) -> str:
    """Selbständiges Beispiel-HTML ohne Zugriff auf den Python-Host übertragen."""
    return "data:text/html;charset=utf-8," + quote(html, safe="")


@contextmanager
def browser_session(repo_root: Path):
    """Vorhandenen Selenium-Dienst nutzen und die Sitzung immer beenden.

    Lokal stellt Docker Compose den Dienst bereit, in Codespaces der
    konfigurierte Nebendienst. Es wird kein Browser/Treiber nachinstalliert.
    """
    remote_url = resolve_browser_url(repo_root)
    _wait_for_selenium(remote_url)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    client = ClientConfig(
        remote_server_addr=remote_url,
        timeout=30,
        proxy=Proxy(raw={"proxyType": ProxyType.DIRECT}),
    )
    connection = RemoteConnection(client_config=client)
    driver = webdriver.Remote(command_executor=connection, options=options)
    body_failed = False
    try:
        driver.set_page_load_timeout(20)
        yield driver
    except BaseException:
        body_failed = True
        raise
    finally:
        try:
            driver.quit()
        except Exception:
            if not body_failed:
                raise RuntimeError(
                    "Browser-Sitzung konnte nicht beendet werden. Prüfe den Selenium-Dienst."
                ) from None
