"""Глобальные фикстуры фреймворка"""

import sys
from os import path
from platform import platform
from typing import Union, Generator, Optional, Callable, Any

import allure
import pytest
from _pytest.fixtures import SubRequest
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Edge

from library.selenium_wrapper import init_chrome, init_firefox, init_edge
from library.test_utils.browser_data import BrowserData
from library.test_utils.stand_data import StandData


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
def driver(browser_data: BrowserData) -> Generator[Union[Chrome, Firefox, Edge], None, None]:
    """Инициализация веб-драйвера"""
    init_browser = {'chrome': init_chrome,
                    'firefox': init_firefox, 'edge': init_edge}
    _driver = init_browser[browser_data.name](browser_data)
    yield _driver
    _driver.quit()


@allure.title('Загрузка переменных стенда')
@pytest.fixture(scope='session')
def stand(variables):
    """Загрузка переменных стенда"""
    try:
        yield StandData(env=variables['stand']['env'])
    except KeyError as k:
        sys.exit(f'Отсутствует секция "{k.args[0]}" в файле данных стенда')


@allure.title('Загрузка переменных браузера')
@pytest.fixture(scope='session')
def browser_data(variables):
    """Загрузка переменных браузера"""
    try:
        variables['browser'].setdefault('cli-arguments', [])
        variables['browser'].setdefault('prefs', [])
        yield BrowserData(name=variables['browser']['name'],
                          version=variables['browser']['version'],
                          cli_args=variables['browser']['cli-arguments'],
                          prefs=variables['browser']['prefs'])
    except KeyError as k:
        sys.exit(f'Отсутствует секция {k.args[0]} в файле данных браузера')


@pytest.fixture(scope='session', autouse=True)
@allure.title('Запись переменных окружения')
def environment(add_allure_env_property: Callable, stand: StandData, browser_data: BrowserData) -> None:
    """Наполнение allure-отчета требуемыми переменными окружения"""
    add_allure_env_property('ENV', stand.env)
    add_allure_env_property('Browser', browser_data.name)
    add_allure_env_property('BrowserVersion', browser_data.version)
    add_allure_env_property('OS', platform())
