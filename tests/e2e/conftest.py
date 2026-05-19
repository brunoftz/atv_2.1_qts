import threading
import time

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from app import create_app


def wait_for_server(url, timeout=10):
    """Espera o servidor Flask subir antes de iniciar os testes."""
    for _ in range(timeout * 10):
        try:
            requests.get(url)
            return
        except Exception:
            time.sleep(0.1)
    raise RuntimeError(f"Servidor não iniciou em {url}")


@pytest.fixture(scope="module")
def live_server():
    app = create_app()
    port = 5001
    base_url = f"http://127.0.0.1:{port}"

    def run_app():
        app.run(
            host="127.0.0.1",
            port=port,
            debug=False,
            use_reloader=False
        )

    thread = threading.Thread(target=run_app, daemon=True)
    thread.start()

    wait_for_server(base_url)

    yield base_url


@pytest.fixture
def browser():
    options = Options()

    # mais compatível com CI e versões diferentes do Chrome
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()