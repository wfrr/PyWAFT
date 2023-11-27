import allure

from config.config import TestData
from library.test_utils.base_test import assert_strings_equal


@allure.title('Проверка входа в личный кабинет обычным пользователем')
def test_user_logon(login_page, account_page):
    login_page.fill_login(TestData.CUSTOMER_EMAIL)
    login_page.fill_password(TestData.CUSTOMER_PASSWORD)
    login_page.do_login()
    assert_strings_equal(value1=account_page.get_title(), value2='My Account',
                         msg='Ошибка проверки входа')
