import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent

options = webdriver.ChromeOptions()

useragent = UserAgent()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--disable-extensions")
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-blink-features")
options.add_argument('--headless')
options.add_argument(f"user-agent={useragent.random}")


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()