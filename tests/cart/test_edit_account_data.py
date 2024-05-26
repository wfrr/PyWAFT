"""Модуль тестов редактирования данных учетной записи"""

from typing import Union

import allure
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver
from sqlalchemy.orm import Session

from library.database.cart import select_customer_by_id
from library.pages.cart import EditAccountPage, AccountPage
from library.test_utils.base import assert_strings_equal
from library.test_utils.cart.cart_data import CartData
from library.test_utils.cart.user_data import PersonInfo


@allure.title('Проверка редактирования поля клиента')
@pytest.mark.edit_account
def test_edit_customer_account_data(
        db_session: Session, driver: Union[ChromeWebDriver, FirefoxWebDriver, EdgeWebDriver],
        edit_customer_page: EditAccountPage, personal_info: PersonInfo, stand: CartData
) -> None:
    """Тест редактирования учетной записи покупателя"""
    with allure.step('Проверка существующих данных клиента'):
        customer = select_customer_by_id(
            db_session, stand.users['customer']['customer_id'])
        assert_strings_equal(value1=edit_customer_page.get_first_name(), value2=customer['firstname'],
                             msg='Ошибка соответствия имени клиента')
        assert_strings_equal(value1=edit_customer_page.get_last_name(), value2=customer['lastname'],
                             msg='Ошибка соответствия фамилии клиента')
        email = edit_customer_page.get_email()
        assert_strings_equal(value1=email, value2=customer['email'],
                             msg='Ошибка соответствия email клиента')

    with allure.step('Проверка обновления данных клиента'):
        edit_customer_page.change_first_name(personal_info.first_name)
        edit_customer_page.change_last_name(personal_info.last_name)
        edit_customer_page.save_changes()
        msg = AccountPage(driver).get_success_msg()
        assert_strings_equal(value1=msg, value2='Success: Your account has been successfully updated.',
                             msg='Ошибка проверки сообщения об успешном сохранении')
        customer = select_customer_by_id(
            db_session, stand.users['customer']['customer_id'])
        assert_strings_equal(value1=customer['firstname'], value2=personal_info.first_name,
                             msg='Ошибка соответствия имени клиента после изменения')
        assert_strings_equal(value1=customer['lastname'], value2=personal_info.last_name,
                             msg='Ошибка соответствия фамилии клиента после изменения')
        assert_strings_equal(value1=email, value2=customer['email'],
                             msg='Ошибка соответствия email клиента после изменения')
