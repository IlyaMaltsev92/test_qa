from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


contacts_locator = ('xpath',"//a[@href='/contacts' and @class='sbisru-Header__menu-link sbisru-Header__menu-link--hover']")
tensor_logo_locator = ('xpath',"//a[@rel='noopener']")


class sbis_MainPage:
    URL = "https://sbis.ru/"

    def __init__(self, browser:webdriver):
        self.browser = browser

    def contact_button(self):
        return self.browser.find_element(*contacts_locator)

    def click_contact_button(self):
        time.sleep(5)
        self.contact_button().click()

