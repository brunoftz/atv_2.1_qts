from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

def test_create_user_e2e():
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000/")

    input_name = driver.find_element(By.ID, "name")
    input_name.send_keys("Maylon")

    button = driver.find_element(By.ID, "submit").click()

    from selenium.webdriver.support.ui import WebDriverWait
    
    wait = WebDriverWait(driver, 5)
  
    wait.until(
        lambda d: any("Maylon" in user.text for user in d.find_elements(By.TAG_NAME, "li"))
    )
    

    # Verificar se o usuário foi criado
    users = driver.find_elements(By.TAG_NAME, "li")
    assert any("Maylon" in user.text for user in users)

    driver.quit()
    
def test_create_two_users_e2e():
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000/")

    wait = WebDriverWait(driver, 5)

    # ---------------------------
    # 1. Criar primeiro usuário
    # ---------------------------
    input_name = driver.find_element(By.ID, "name")
    input_name.clear()
    input_name.send_keys("Maylon")

    driver.find_element(By.ID, "submit").click()

    # aguardar aparecer na lista
    wait.until(
        lambda d: any("Maylon" in el.text for el in d.find_elements(By.TAG_NAME, "li"))
    )

    
    input_name = driver.find_element(By.ID, "name")
    input_name.clear()
    input_name.send_keys("Bruno")

    driver.find_element(By.ID, "submit").click()

    
    wait.until(
        lambda d: any("Bruno" in el.text for el in d.find_elements(By.TAG_NAME, "li"))
    )

    users = driver.find_elements(By.TAG_NAME, "li")
    texts = [u.text for u in users]

    assert "Maylon" in texts
    assert "Bruno" in texts
    
    driver.quit()
    
    
def test_user_flow_e2e():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)


    driver.get("http://localhost:5000/")


    assert "Users" in driver.title

    input_name = driver.find_element(By.ID, "name")

    input_name.send_keys("User1")

    driver.find_element(By.ID, "submit").click()

    wait.until(
        lambda d: any("User1" in el.text for el in d.find_elements(By.TAG_NAME, "li"))
    )

    users = driver.find_elements(By.TAG_NAME, "li")
    assert any("User1" in u.text for u in users)

    input_name = driver.find_element(By.ID, "name")
    input_name.clear()
    input_name.send_keys("User2")

    driver.find_element(By.ID, "submit").click()

    wait.until(
        lambda d: any("User2" in el.text for el in d.find_elements(By.TAG_NAME, "li"))
    )

    users = driver.find_elements(By.TAG_NAME, "li")
    texts = [u.text for u in users]

    assert "User1" in texts
    assert "User2" in texts

    driver.quit()