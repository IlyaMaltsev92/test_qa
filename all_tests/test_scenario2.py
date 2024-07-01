from pages.contacts_page import sbis_ContactsPage

def test_region(browser):
    browser.get(sbis_ContactsPage.URL)
    contacts_page = sbis_ContactsPage(browser)
    assert contacts_page.browser.current_url == "https://sbis.ru/contacts/39-kaliningradskaya-oblast?tab=clients" , 'Wrong region'

def test_partners_list_not_empty(browser):
    browser.get(sbis_ContactsPage.URL)
    contacts_page = sbis_ContactsPage(browser)
    partners = contacts_page.get_partners_list()
    assert len(partners) != 0, 'No partners'

def test_change_region(browser):
    browser.get(sbis_ContactsPage.URL)
    contacts_page = sbis_ContactsPage(browser)

    contacts_page.click_region_chooser()
    contacts_page.click_kamch_krai()

    partners_list = contacts_page.get_partners_list()
    expected_title = 'СБИС - Камчатка'
    assert contacts_page.browser.current_url == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients", 'Wrong Region'
    assert partners_list[0].text == expected_title

