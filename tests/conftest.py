from typing import Generator, Union, Mapping

import allure
import pytest

from selenium.webdriver.chrome.webdriver import WebDriver
from sqlalchemy.orm import Session

from library.database.queries import select_customers_order_by_firstname
from library.pages.admin_login_page import AdminLoginPage
from library.pages.edit_account_page import EditAccountPage
from library.pages.main_page import MainPage
from library.pages.login_page import LoginPage
from library.pages.account_page import AccountPage


@pytest.fixture(scope='module')
@allure.title('Открытие главной страницы')
def main_page(
        driver: WebDriver, variables: Mapping[str, Union[str, Mapping[str, Mapping[str, Union[str, int]]]]]
) -> Generator[MainPage, None, None]:
    driver.get(variables['app']['url'])
    yield MainPage(driver)


@pytest.fixture(scope='module')
@allure.title('Открытие страницы входа администратора')
def admin_login_page(
        driver: WebDriver, variables: Mapping[str, Union[str, Mapping[str, Mapping[str, Union[str, int]]]]]
) -> Generator[AdminLoginPage, None, None]:
    driver.get(variables['users']['admin']['url'])
    yield AdminLoginPage(driver)


@pytest.fixture(scope='module')
@allure.title('Переход на страницу логина')
def login_page(main_page: MainPage, driver: Union[WebDriver]) -> Generator[LoginPage, None, None]:
    main_page.open_account_options()
    main_page.select_login()
    yield LoginPage(driver)


@pytest.fixture(scope='module')
@allure.title('Авторизация клиента')
def account_page(
        driver: WebDriver,
        login_page: LoginPage,
        variables: Mapping[str, Union[str, Mapping[str, Mapping[str, Union[str, int]]]]]
) -> Generator[AccountPage, None, None]:
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
    account_page.edit_account_page()
    yield EditAccountPage(driver)


@pytest.fixture(scope='module')
@allure.title('Получение содержимого корзины клиента')
def shopping_cart_content(db_session: Session) -> Generator[list[Mapping[str, Union[str, int]]], None, None]:
    yield select_customers_order_by_firstname(db_session)
