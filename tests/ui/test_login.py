"""Модуль тестов для проверки входа."""

import allure
import pytest

from mealie.app_data import AppData
from mealie.pages.login_page import LoginPage


@allure.tag('login')
@allure.title('Проверка входа в пользователя')
@pytest.mark.login
def test_user_logon(login_page: LoginPage, stand: AppData) -> None:
    """Тест проверки входа."""
    home_page = login_page.login_user(stand.users['regular']['email'], stand.users['regular']['password'])
    assert home_page.get_title() == 'Mealie', 'Ошибка проверки входа'
