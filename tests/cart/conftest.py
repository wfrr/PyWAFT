"""Вспомогательные фикстуры для тестов OpenCart"""
from typing import Generator, Union, Mapping

import allure
import pytest
import sys

from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Edge
from sqlalchemy.orm import Session

from library.database.cart import select_customers_order_by_firstname, init_db_connection
from library.pages.cart import MainPage, AdminLoginPage, LoginPage, AccountPage, EditAccountPage
from library.test_utils.cart.cart_data import CartData
from library.test_utils.cart.user_data import PersonInfo
from library.test_utils.cart.utils import random_string


@pytest.fixture(scope='module')
@allure.title('Инициализация подключения к БД')
def db_session(stand: CartData) -> Generator[Session, None, None]:
    """Инициализация подключения к БД"""
    db_conf = {
        'username': stand.db['username'],
        'password': stand.db['password'],
        'host': stand.db['host'],
        'port': stand.db['port'],
        'db_name': stand.db['name']
    }
    yield init_db_connection(db_conf)


@allure.title('Загрузка переменных стенда')
@pytest.fixture(scope='session')
def stand(variables):
    """Загрузка переменных стенда"""
    try:
        yield CartData(env=variables['stand']['env'], app=variables['stand']['app'],
                       db=variables['stand']['db'], users=variables['stand']['users'])
    except KeyError as k:
        sys.exit(f'Отсутствует секция "{k.args[0]}" в файле данных стенда')


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


@pytest.fixture(scope='module')
@allure.title('Открытие главной страницы')
def main_page(driver: Union[Chrome, Firefox, Edge], stand: CartData) -> Generator[MainPage, None, None]:
    """Открытие главной страницы"""
    driver.get(stand.app['url'])
    yield MainPage(driver)


@pytest.fixture(scope='module')
@allure.title('Открытие страницы входа администратора')
def admin_login_page(driver: Union[Chrome, Firefox, Edge], stand: CartData) -> Generator[AdminLoginPage, None, None]:
    """Открытие страницы авторизации администратора"""
    driver.get(stand.users['admin']['url'])
    yield AdminLoginPage(driver)


@pytest.fixture(scope='module')
@allure.title('Переход на страницу логина')
def login_page(main_page: MainPage, driver: Union[Chrome, Firefox, Edge]) -> Generator[LoginPage, None, None]:
    """Открытие страницы входа клиента"""
    main_page.open_account_options()
    main_page.select_login()
    yield LoginPage(driver)


@pytest.fixture(scope='module')
@allure.title('Авторизация клиента')
def account_page(
        driver: Union[Chrome, Firefox, Edge], login_page: LoginPage, stand: CartData
) -> Generator[AccountPage, None, None]:
    """Открытие страницы личного кабинета клиента"""
    login_page.fill_login(stand.users['customer']['email'])
    login_page.fill_password(stand.users['customer']['password'])
    login_page.do_login()
    yield AccountPage(driver)


@pytest.fixture(scope='module')
@allure.title('Редактирование данных клиента')
def edit_customer_page(
        account_page: AccountPage, driver: Union[Chrome, Firefox, Edge]
) -> Generator[EditAccountPage, None, None]:
    """Открытие страницы редактирования данных клиента"""
    account_page.edit_account_page()
    yield EditAccountPage(driver)


@pytest.fixture(scope='module')
@allure.title('Получение содержимого корзины клиента')
def shopping_cart_content(db_session: Session) -> Generator[list[Mapping[str, Union[str, int]]], None, None]:
    """Получение содержимого корзины клиента"""
    yield select_customers_order_by_firstname(db_session)
