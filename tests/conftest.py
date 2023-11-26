import allure
import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
@allure.title('Инициализация веб драйвера')
def driver(request):
    # load appropriate browser version
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver

    yield chrome_driver

    # teardown browser
    chrome_driver.quit()
