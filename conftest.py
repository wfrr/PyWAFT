from typing import Mapping, Union, Generator

import allure
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver
from sqlalchemy.orm import Session

from library.database.connection import init_db_connection
from library.selenium_wrapper import init_chrome, init_firefox, init_edge
from library.utils import random_string


@pytest.fixture(scope='module')
@allure.title('Инициализация веб драйвера')
def driver(
        variables: Mapping[str, Union[str, Mapping[str, Mapping[str, Union[str, int]]]]]
) -> Generator[Union[ChromeWebDriver, FirefoxWebDriver, EdgeWebDriver], None, None]:
    browser = {'chrome': init_chrome, 'firefox': init_firefox, 'edge': init_edge}
    _driver = browser[variables['capabilities']['browser']](variables['capabilities']['browser_version'])
    yield _driver
    _driver.quit()


@pytest.fixture(scope='module')
@allure.title('Инициализация подключения к БД')
def db_session(
        variables: Mapping[str, Union[str, Mapping[str, Mapping[str, Union[str, int]]]]]
) -> Generator[Session, None, None]:
    db_conf = {
        'username': variables['database']['username'],
        'password': variables['database']['password'],
        'host': variables['database']['host'],
        'port': variables['database']['port'],
        'db_name': variables['database']['db_name']
    }
    yield init_db_connection(db_conf)


@pytest.fixture(scope='module')
@allure.title('Генерация имени')
def random_first_name():
    yield random_string(5)


@pytest.fixture(scope='module')
@allure.title('Генерация фамилии')
def random_last_name():
    yield random_string(8)
