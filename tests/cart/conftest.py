"""Вспомогательные фикстуры для тестов OpenCart"""

from typing import Generator, Union, Mapping

import allure
import pytest

from selenium.webdriver.chrome.webdriver import WebDriver
from sqlalchemy.orm import Session

from library.database.cart import select_customers_order_by_firstname
from library.pages.cart import MainPage, AdminLoginPage, LoginPage, AccountPage, EditAccountPage


@pytest.fixture(scope='module')
@allure.title('Открытие главной страницы')
def main_page(
        driver: WebDriver, variables: Mapping[str, Union[str, Mapping[str, Mapping[str, Union[str, int]]]]]
) -> Generator[MainPage, None, None]:
    """Открытие главной страницы"""
    driver.get(variables['app']['url'])
    yield MainPage(driver)


@pytest.fixture(scope='module')
@allure.title('Открытие страницы входа администратора')
def admin_login_page(
        driver: WebDriver, variables: Mapping[str, Union[str, Mapping[str, Mapping[str, Union[str, int]]]]]
) -> Generator[AdminLoginPage, None, None]:
    """Открытие страницы авторизации администратора"""
    driver.get(variables['users']['admin']['url'])
    yield AdminLoginPage(driver)


@pytest.fixture(scope='module')
@allure.title('Переход на страницу логина')
def login_page(main_page: MainPage, driver: Union[WebDriver]) -> Generator[LoginPage, None, None]:
    """Открытие страницы входа клиента"""
    main_page.open_account_options()
    main_page.select_login()
    yield LoginPage(driver)


@pytest.fixture(scope='module')
@allure.title('Авторизация клиента')
def account_page(
        driver: WebDriver,
        login_page: LoginPage,
        variables: Mapping[str, Union[str,
                                      Mapping[str, Mapping[str, Union[str, int]]]]]
) -> Generator[AccountPage, None, None]:
    """Открытие страницы личного кабинета клиента"""
    login_page.fill_login(variables['users']['customer']['email'])
    login_page.fill_password(variables['users']['customer']['password'])
    login_page.do_login()
    yield AccountPage(driver)


@pytest.fixture(scope='module')
@allure.title('Редактирование данных клиента')
def edit_customer_page(
        account_page: AccountPage,
        driver: WebDriver,
) -> Generator[EditAccountPage, None, None]:
    """Открытие страницы редактирования данных клиента"""
    account_page.edit_account_page()
    yield EditAccountPage(driver)


@pytest.fixture(scope='module')
@allure.title('Получение содержимого корзины клиента')
def shopping_cart_content(db_session: Session) -> Generator[list[Mapping[str, Union[str, int]]], None, None]:
    """Получение содержимого корзины клиента"""
    yield select_customers_order_by_firstname(db_session)
