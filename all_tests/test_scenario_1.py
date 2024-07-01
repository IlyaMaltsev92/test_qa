from pages.contacts_page import sbis_ContactsPage
from pages.sbis_ru import sbis_MainPage
from pages.tensor_ru import tensor_MainPage,tensor_AboutPage
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

def test_sbis_main_page(browser):
    browser.get(sbis_MainPage.URL)
    main_page = sbis_MainPage(browser)

    assert browser.current_url == "https://sbis.ru/"
    contacts = main_page.contact_button()
    contacts.click()
    assert browser.current_url == "https://sbis.ru/contacts"

def test_contacts_page(browser):
    browser.get(sbis_ContactsPage.URL)
    contacts_page = sbis_ContactsPage(browser)

    tensor_logo_button = contacts_page.tensor_logo()

    tensor_logo_button.click()
    assert browser.current_url == "https://sbis.ru/contacts/39-kaliningradskaya-oblast?tab=clients"

def test_tensor_main_page(browser):
    browser.get(tensor_MainPage.URL)
    main_page = tensor_MainPage(browser)

    assert main_page.power_in_people_block().text.startswith('Сила в людях')

    main_page.more_detail_button()
    main_page.click_details_button()

    assert browser.current_url == "https://tensor.ru/about"

def test_tensor_about_page(browser):
    browser.get(tensor_AboutPage.URL)
    about_page = tensor_AboutPage(browser)

    pics = about_page.get_pictures()

    heights = [int(i.get_attribute('height')) for i in pics]
    widths = [int(i.get_attribute('width')) for i in pics]

    expected_heights = [193,193,193,193]
    expected_widths = [272,272,272,272]

    assert len(pics) == 4
    assert heights == expected_heights
    assert widths == expected_widths

