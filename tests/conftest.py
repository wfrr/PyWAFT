from typing import Generator, Union, Dict

import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from library.pages.main_page import MainPage
from library.pages.login_page import LoginPage
from library.pages.account_page import AccountPage


@pytest.fixture(scope='module')
@allure.title('Инициализация веб драйвера')
def driver(variables: Dict[str, Union[str, Dict[str, Dict[str, str]]]]) -> Generator[WebDriver, None, None]:
    _driver = webdriver.Chrome()
    # TODO: logging
    print(f'Запуск теста на стенде: {variables["stand"]}')
    yield _driver
    _driver.quit()


@pytest.fixture(scope='module')
@allure.title('Открытие главной страницы')
def main_page(
        driver: WebDriver, variables: Dict[str, Union[str, Dict[str, Dict[str, str]]]]
) -> Generator[MainPage, None, None]:
    driver.get(variables['app']['url'])
    yield MainPage(driver)


@pytest.fixture(scope='module')
@allure.title('Открытие главной страницы')
def account_page(driver: webdriver) -> Generator[AccountPage, None, None]:
    yield AccountPage(driver)


@pytest.fixture(scope='module')
@allure.title('Переход на страницу логина')
def login_page(main_page: MainPage, driver: Union[WebDriver]) -> Generator[LoginPage, None, None]:
    main_page.open_account_options()
    main_page.select_login()
    yield LoginPage(driver)
