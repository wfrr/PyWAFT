import allure
import pytest
from selenium import webdriver

from config.config import TestData
from library.pages.main_page import MainPage
from library.pages.login_page import LoginPage
from library.pages.account_page import AccountPage


@pytest.fixture(scope='class')
@allure.title('Инициализация веб драйвера')
def driver(request):
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()


@pytest.fixture(scope='class')
@allure.title('Открытие главной страницы')
def main_page(driver):
    # TODO: передача URL
    driver.get(TestData.URL)
    yield MainPage(driver)


@pytest.fixture(scope='class')
@allure.title('Открытие главной страницы')
def account_page(driver):
    yield AccountPage(driver)


@pytest.fixture(scope='class')
@allure.title('Переход на страницу логина')
def login_page(main_page, driver):
    main_page.open_account_options()
    main_page.select_login()
    yield LoginPage(driver)
