"""Модуль теста корзины покупателя"""

from typing import Mapping, Union

import allure
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver

from library.pages.cart import AccountPage, ShoppingCartPage
from library.test_utils.base import assert_strings_equal


@allure.title('Просмотр корзины клиента')
@pytest.mark.shopping_cart
def test_view_shopping_cart(
        account_page: AccountPage, driver: Union[ChromeWebDriver, FirefoxWebDriver, EdgeWebDriver],
        shopping_cart_content: list[Mapping[str, Union[str, int]]]
) -> None:
    """Тест просмотра корзины клиента"""
    account_page.open_shopping_cart()
    cart_data = ShoppingCartPage(driver).get_n_entries(
        len(shopping_cart_content))
    for entry, exp_entry in zip(cart_data, shopping_cart_content):
        for key, value in exp_entry.items():
            if key not in entry.keys():
                raise AssertionError(f'Отсутствует ожидаемое поле {key}')
            assert_strings_equal(value1=entry[key], value2=str(
                value), msg=f'Ошибка проверки {key}')
