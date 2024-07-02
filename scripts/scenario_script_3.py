import time

from pages.sbis_ru import sbis_MainPage,DownloadPage
import os
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--incognito')
# chrome_options.add_argument('--window-size=1920,1080')
# service = Service(executable_path=ChromeDriverManager().install())
#
# browser = webdriver.Chrome(service=service, options=chrome_options)

path = 'C:\\Users\ILYA\Downloads\sbisplugin-setup-web.exe'



browser.get(sbis_MainPage.URL)
main_page = sbis_MainPage(browser)
local_versions = main_page.download_local_versions()

browser.execute_script("arguments[0].scrollIntoView(true);", local_versions)
main_page.click_download_local_versions()

download_page = DownloadPage(browser)
ref = download_page.download_button()
download_page.click_download_button()
expected_size = float(ref.text[13:17])

time.sleep(10)
file_size = os.path.getsize(path)
expected_size = float(download_butt.text[13:17])
real_size = file_size/1024
real_size /= 1024
assert round(real_size,2) == expected_size
print('test_passed')
