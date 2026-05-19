import threading
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from app import create_app


@pytest.fixture(scope="module")
def live_server():
    app = create_app()
    port = 5001

    def run_app():
        app.run(host="127.0.0.1", port=port, debug=False, use_reloader=False)

    thread = threading.Thread(target=run_app, daemon=True)
    thread.start()
    time.sleep(1)
    yield f"http://127.0.0.1:{port}"


@pytest.fixture
def browser():
    options = Options()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
