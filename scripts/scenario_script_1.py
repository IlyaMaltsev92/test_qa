from pages.contacts_page import sbis_ContactsPage
from pages.sbis_ru import sbis_MainPage
from pages.tensor_ru import tensor_MainPage,tensor_AboutPage

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

expected_heights = [193, 193, 193, 193]
expected_widths = [272, 272, 272, 272]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--window-size=1920,1080')
service = Service(executable_path=ChromeDriverManager().install())

chrome_browser = webdriver.Chrome(service=service, options=chrome_options)

chrome_browser.get(sbis_MainPage.URL)
main_page = sbis_MainPage(chrome_browser)

contacts = main_page.contact_button()
contacts.click()

contacts_page = sbis_ContactsPage(chrome_browser)

tensor_logo_button = contacts_page.tensor_logo()

contacts_page.click_tensor_logo()

main_page = tensor_MainPage(chrome_browser)

main_page.more_detail_button()
main_page.click_details_button()

about_page = tensor_AboutPage(chrome_browser)

pics = about_page.get_pictures()

heights = [int(i.get_attribute('height')) for i in pics]
widths = [int(i.get_attribute('width')) for i in pics]


assert len(pics) == 4
assert heights == expected_heights
assert widths == expected_widths
print('All all_tests passed')
