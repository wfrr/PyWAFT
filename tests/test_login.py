from typing import Dict, Union

import allure

from library.pages.account_page import AccountPage
from library.pages.login_page import LoginPage
from library.test_utils.base import assert_strings_equal


@allure.tag('login')
@allure.title('Проверка входа в личный кабинет обычным пользователем')
def test_user_logon(login_page: LoginPage, account_page: AccountPage,
                    variables: Dict[str, Union[str, Dict[str, Dict[str, str]]]]) -> None:
    login_page.fill_login(variables['users']['customer']['email'])
    login_page.fill_password(variables['users']['customer']['password'])
    login_page.do_login()
    assert_strings_equal(value1=account_page.get_title(), value2='My Account', msg='Ошибка проверки входа')
