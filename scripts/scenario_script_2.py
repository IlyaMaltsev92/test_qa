from pages.contacts_page import sbis_ContactsPage
from pages.sbis_ru import sbis_MainPage


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--incognito')
# chrome_options.add_argument('--window-size=1920,1080')
# service = Service(executable_path=ChromeDriverManager().install())
# chrome_browser = webdriver.Chrome(service=service, options=chrome_options)

expected_title = 'СБИС - Камчатка'
chrome_browser.get(sbis_MainPage.URL)
main_page = sbis_MainPage(chrome_browser)

main_page.click_contact_button()

contacts_page = sbis_ContactsPage(chrome_browser)
partners = contacts_page.get_partners_list()
assert len(partners) != 0, 'No partners'


contacts_page.click_region_chooser()
contacts_page.click_kamch_krai()

partners_list = contacts_page.get_partners_list()

assert contacts_page.browser.current_url == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients", 'Wrong Region'
assert partners_list[0].text == expected_title , 'Wront title'



