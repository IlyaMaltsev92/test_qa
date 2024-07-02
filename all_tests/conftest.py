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
