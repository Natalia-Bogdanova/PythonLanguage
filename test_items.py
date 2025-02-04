import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_availability_button_add_to_cart_(browser):
    browser.get(link)
    time.sleep(30)
    add_to_basket_button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    # Проверяем, что кнопка найдена и она единственная
    assert len(add_to_basket_button) == 1, "Кнопка должна быть единственной"
