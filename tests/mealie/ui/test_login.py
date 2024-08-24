"""Модуль тестов для проверки входа"""

import allure
from pytest import mark

from library.pages.mealie.login_page import LoginPage
from library.test_utils.mealie.app_data import AppData


@allure.tag('login')
@allure.title('Проверка входа в пользователя')
@mark.login
def test_user_logon(login_page: LoginPage, stand: AppData) -> None:
    """Тест проверки входа"""
    home_page = login_page.login_user(stand.users['regular']['email'], stand.users['regular']['password'])
    assert home_page.get_title() == 'Mealie', 'Ошибка проверки входа'
