from selenium.webdriver.common.by import By
import time


def test_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30) # держи слип братулёк :)
    elem = browser.find_element(By.ID, "id_quantity")
    assert elem, 'видишь кнопку? и я нет'
