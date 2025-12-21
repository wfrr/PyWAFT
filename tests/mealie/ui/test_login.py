"""Модуль тестов для проверки входа."""

import allure
import pytest

from library.assertions.common import assert_strings_equal
from library.core.app_data import AppData
from library.mealie.pages.login_page import LoginPage


@allure.title("Проверка входа в пользователя")
@pytest.mark.ui
@pytest.mark.login
def test_user_logon(login_page: LoginPage, stand: AppData) -> None:
    """Тест проверки входа."""
    home_page = login_page.login_user(
        stand.users["regular"]["email"], stand.users["regular"]["password"]
    )
    assert_strings_equal(home_page.get_title(), "Mealie", "Ошибка проверки входа")
