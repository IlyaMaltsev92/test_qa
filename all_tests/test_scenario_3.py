import time

from pages.sbis_ru import sbis_MainPage,DownloadPage
import os
path = 'C:\\Users\ILYA\Downloads\sbisplugin-setup-web.exe'

def test_right_ref(browser):
    browser.get(sbis_MainPage.URL)
    main_page = sbis_MainPage(browser)
    local_versions = main_page.download_local_versions()
    assert local_versions.text == 'Скачать локальные версии'

def test_right_url_after_click(browser):
    browser.get(sbis_MainPage.URL)
    main_page = sbis_MainPage(browser)
    local_versions = main_page.download_local_versions()
    browser.execute_script("arguments[0].scrollIntoView(true);", local_versions)
    main_page.click_download_local_versions()
    assert browser.current_url == 'https://sbis.ru/download'

def test_right_download_ref(browser):
    browser.get(DownloadPage.URL)
    download_page = DownloadPage(browser)
    ref = download_page.download_button()
    assert ref.text == "Скачать (Exe 7.22 МБ)"

def test_right_size_after_download(browser):
    browser.get(DownloadPage.URL)
    download_page = DownloadPage(browser)
    download_butt = download_page.download_button()
    download_page.click_download_button()
    time.sleep(10)
    expected_size = float(download_butt.text[13:17])
    file_size = os.path.getsize(path)
    real_size = file_size/1024
    real_size /= 1024
    assert round(real_size,2) == expected_size
