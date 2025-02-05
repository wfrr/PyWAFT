"""Модуль тестов для проверки входа."""

import allure
import pytest

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
    with allure.step("Проверка соответствия заголовка стрраницы"):
        assert home_page.get_title() == "Mealie", "Ошибка проверки входа"
