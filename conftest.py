"""Глобальные фикстуры фреймворка"""

import platform
from os import path
from typing import Mapping, Union, Generator, Optional, Callable, Any

import allure
import pytest
from _pytest.fixtures import SubRequest
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver
from sqlalchemy.orm import Session

from library.database.cart import init_db_connection
from library.selenium_wrapper import init_chrome, init_firefox, init_edge
from library.test_utils.user_data import PersonInfo
from library.utils import random_string


ALLURE_ENVIRONMENT_PROPERTIES_FILE = 'environment.properties'
ALLUREDIR_OPTION = '--alluredir'


@pytest.fixture(scope='session', autouse=True)
def add_allure_env_property(request: SubRequest) -> Optional[Callable]:
    """Наполнение файла переменных окружения для allure-отчета"""
    environment_properties = {}

    def maker(key: str, value: Any):
        environment_properties.update({key: value})

    yield maker

    alluredir = request.config.getoption(ALLUREDIR_OPTION)
    if not alluredir or not path.isdir(alluredir) or not environment_properties:
        return
    allure_env_path = path.join(alluredir, ALLURE_ENVIRONMENT_PROPERTIES_FILE)
    with open(allure_env_path, 'w', encoding='utf-8') as _f:
        data = '\n'.join([f'{variable}={value}' for variable,
                         value in environment_properties.items()])
        _f.write(data)


@pytest.fixture(scope='module')
@allure.title('Инициализация веб драйвера')
def driver(
        variables: Mapping[str, Union[str,
                                      Mapping[str, Mapping[str, Union[str, int]]]]]
) -> Generator[Union[ChromeWebDriver, FirefoxWebDriver, EdgeWebDriver], None, None]:
    """Инициализация вебдрайвера"""
    browser = {'chrome': init_chrome,
               'firefox': init_firefox, 'edge': init_edge}
    _driver = browser[variables['capabilities']['browser']](
        variables['capabilities']['browser_version'])
    yield _driver
    _driver.quit()


@pytest.fixture(scope='module')
@allure.title('Инициализация подключения к БД')
def db_session(
        variables: Mapping[str, Union[str,
                                      Mapping[str, Mapping[str, Union[str, int]]]]]
) -> Generator[Session, None, None]:
    """Инициализация подключения к БД"""
    db_conf = {
        'username': variables['database']['username'],
        'password': variables['database']['password'],
        'host': variables['database']['host'],
        'port': variables['database']['port'],
        'db_name': variables['database']['db_name']
    }
    yield init_db_connection(db_conf)


@pytest.fixture(scope='session', autouse=True)
@allure.title('Запись переменных окружения')
def environment(add_allure_env_property: Callable,
                variables: Mapping[str, Union[str, Mapping[str, Mapping[str, Union[str, int]]]]]) -> None:
    """Наполнение allure-отчета требуемыми переменными окружения"""
    add_allure_env_property('ENV', variables['environment'])
    add_allure_env_property('Browser', variables['capabilities']['browser'])
    add_allure_env_property(
        'Browser-version', variables['capabilities']['browser_version'])
    add_allure_env_property('OS', platform.platform())


@pytest.fixture(scope='module')
@allure.title('Генерация имени')
def random_first_name():
    """Фикстура генерации случайного имени"""
    yield random_string(5)


@pytest.fixture(scope='module')
@allure.title('Генерация фамилии')
def random_last_name():
    """Фикстура генерации случайной фамилии"""
    yield random_string(8)


@pytest.fixture(scope='module')
@allure.title('Генерация персональных данных')
def personal_info(random_first_name: str, random_last_name: str):
    """Фикстура генерации персональной информации"""
    yield PersonInfo(first_name=random_first_name, last_name=random_last_name)
