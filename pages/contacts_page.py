from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

tensor_logo_locator = ('xpath',"//a[@rel='noopener']")
region_chooser_locator = ('xpath',"//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")
partners_list_locator = ('xpath',"//div[contains(@class,'pr-xm-32')]")
kamchatskiy_krai_locator = ('xpath',"//*[@id='popup']/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span")


class sbis_ContactsPage:

    URL = "https://sbis.ru/contacts/"

    def __init__(self,browser):
        self.browser = browser

    def tensor_logo(self):
        logo = self.browser.find_elements(*tensor_logo_locator)
        return logo[2]

    def click_tensor_logo(self):
        WebDriverWait(self.browser,10,poll_frequency=1).until(EC.url_contains("tab=clients"))
        self.tensor_logo().click()
        self.browser.switch_to.window(self.browser.window_handles[1])

    def region_chooser(self):
        region = self.browser.find_element(*region_chooser_locator)
        return region

    def click_region_chooser(self):
        self.region_chooser().click()

        WebDriverWait(self.browser, 10, poll_frequency=1).until(
            EC.visibility_of_element_located(('xpath', '//ul[@class="sbis_ru-Region-Panel__list-l"]')))

    def get_partners_list(self):
        partners_list = self.browser.find_elements(*partners_list_locator)
        return partners_list

    def click_kamch_krai(self):

        kamchatka = self.browser.find_element(*kamchatskiy_krai_locator)
        kamchatka.click()
        WebDriverWait(self.browser,10).until(EC.url_contains('41'))


