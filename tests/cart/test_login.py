"""Модуль тестов для проверки входа"""

from typing import Union

import allure
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver

from library.pages.cart import AccountPage, LoginPage
from library.test_utils.base import assert_strings_equal
from library.test_utils.cart.cart_data import CartData


@allure.tag('login')
@allure.title('Проверка входа в личный кабинет клиента')
@pytest.mark.login
def test_user_logon(
        driver: Union[ChromeWebDriver, FirefoxWebDriver, EdgeWebDriver], login_page: LoginPage, stand: CartData
) -> None:
    """Тест проверки входа"""
    login_page.fill_login(stand.users['customer']['email'])
    login_page.fill_password(stand.users['customer']['password'])
    login_page.do_login()
    assert_strings_equal(value1=AccountPage(driver).get_title(
    ), value2='My Account', msg='Ошибка проверки входа')
