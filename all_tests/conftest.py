import time
from pprint import pprint

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def browser():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')

    service = Service(executable_path=ChromeDriverManager().install())
    chrome_browser = webdriver.Chrome(service=service, options=chrome_options)
    chrome_browser.implicitly_wait(10)

    return chrome_browser


# driver = browser()
# driver.get("https://sbis.ru/contacts/")
# region = driver.find_element('xpath',"//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")
# region.click()
# kamchatka = driver.find_element('xpath',"//span[@title='Камчатский край']")
# print(kamchatka)
# time.sleep(10)
# driver.execute_script("arguments[0].scrollIntoView(true);",div)
# WebDriverWait(driver,20).until(EC.visibility_of_element_located(('xpath','//img[@alt="Сопровождаем клиентов"]')))
# elements = driver.find_elements('xpath',"//img[@class='tensor_ru-About__block3-image new_lazy loaded']")
# # time.sleep(2)
# pprint(len(elements))