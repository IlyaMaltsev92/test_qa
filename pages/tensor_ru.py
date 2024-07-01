import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

power_in_people_locator = ('xpath',"//div[@class='tensor_ru-Index__block4-content tensor_ru-Index__card']")
more_details_locator = ('xpath','//a[contains(text(),"Подробнее")]')

pictures_locator = ('xpath',"//img[@class='tensor_ru-About__block3-image new_lazy loaded']")
div_works_locator = ('xpath','//div[@class="tensor_ru-container tensor_ru-section tensor_ru-About__block3"]')


class tensor_MainPage():

    URL = 'https://tensor.ru'

    def __init__(self,browser):
        self.browser = browser

    def power_in_people_block(self) :
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(power_in_people_locator))
        return self.browser.find_element(*power_in_people_locator)

    def more_detail_button(self):
        return self.browser.find_elements(*more_details_locator)[2]

    def click_details_button(self):
        self.browser.execute_script("arguments[0].scrollIntoView(true);", self.more_detail_button())
        WebDriverWait(self.browser,10,poll_frequency=1).until(EC.element_to_be_clickable(self.more_detail_button()))
        self.more_detail_button().click()



class tensor_AboutPage:

    URL = "https://tensor.ru/about"

    def __init__(self,browser):
        self.browser = browser

    def get_works(self):
        '''
        возвращает блок div c title Работаем
        :return:
        '''
        div_works = self.browser.find_element(*div_works_locator)
        return div_works

    def get_pictures(self):
        self.browser.execute_script("arguments[0].scrollIntoView(true);",self.get_works())
        WebDriverWait(self.browser,20).until(EC.visibility_of_all_elements_located(pictures_locator))
        time.sleep(5)
        pics = self.browser.find_elements(*pictures_locator)
        return pics

