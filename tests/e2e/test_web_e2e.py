import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.e2e
def test_home_page_displays_title(live_server, browser):
    browser.get(live_server)
    title = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "app-title"))
    )
    assert title.text == "Users App"


@pytest.mark.e2e
def test_status_link_navigates_to_status_page(live_server, browser):
    browser.get(live_server)
    link = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "status-link"))
    )
    link.click()

    status = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "status-text"))
    )
    assert status.text == "ok"
