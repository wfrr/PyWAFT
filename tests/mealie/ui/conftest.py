"""Фикстуры автотестов Mealie"""

import sys
from platform import platform
from typing import Callable, Generator, Union

import allure
from pytest import fixture
from selenium.webdriver import Chrome, Edge, Firefox
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from library.pages.mealie.login_page import LoginPage
from library.selenium_wrapper import init_chrome, init_edge, init_firefox
from library.test_utils.browser_data import BrowserData
from library.test_utils.mealie.app_data import AppData
from library.test_utils.page_factory import page_factory


@fixture(scope='session', autouse=True)
@allure.title('Запись переменных окружения')
def environment(
    add_allure_env_property: Callable, stand: AppData, browser_data: BrowserData
) -> None:
    """Наполнение allure-отчета требуемыми переменными окружения"""
    add_allure_env_property('ENV', stand.app['env'])
    add_allure_env_property('Browser', browser_data.name)
    add_allure_env_property('BrowserVersion', browser_data.version)
    add_allure_env_property('OS', platform())


@allure.title('Загрузка переменных стенда')
@fixture(scope='session')
def stand(variables) -> Generator[AppData, None, None]:
    """Загрузка переменных стенда"""
    try:
        yield AppData(
            app=variables['app'],
            db=variables['app']['db'],
            users=variables['app']['users'],
        )
    except KeyError as k:
        sys.exit(f'Отсутствует секция "{k.args[0]}" в файле данных стенда')


@fixture(scope='function')
@allure.title('Инициализация веб драйвера')
def driver(
    browser_data: BrowserData,
) -> Generator[Union[Chrome, Firefox, Edge], None, None]:
    """Инициализация веб-драйвера"""
    init_browser = {'chrome': init_chrome, 'firefox': init_firefox, 'edge': init_edge}
    _driver = init_browser[browser_data.name](browser_data)
    yield _driver
    _driver.quit()


@fixture(scope='function')
@allure.title('Переход на страницу логина')
def login_page(
    driver: Union[Chrome, Firefox, Edge], stand: AppData
) -> Generator[LoginPage, None, None]:
    """Открытие страницы входа покупателя"""
    driver.get(stand.app['url'])
    yield page_factory(driver, LoginPage)


@fixture(scope='function')
@allure.title('Инициализация подключения к БД')
def orm_db_session(stand: AppData) -> Generator[Session, None, None]:
    """Инициализация подключения к БД с использованием ORM"""
    conf = stand.db
    engine_ = create_engine(
        f'postgresql+psycopg2://{conf["username"]}:{conf["password"]}@{conf["host"]}:{conf["port"]}/{conf["name"]}',
        echo=False,
        pool_size=5,
        max_overflow=10,
    )
    yield Session(bind=engine_)
