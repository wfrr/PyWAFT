"""Модуль тестов списка покупок."""

import allure
import pytest

from library.assertions.common import assert_lists_equal
from library.mealie.pages.shopping_lists_page import ShoppingListsPage


@allure.title("Проверка списка покупок пользователя")
@pytest.mark.parametrize("shopping_list", ["birthday party"], indirect=True)
@pytest.mark.ui
@pytest.mark.shopping_list
def test_user_shopping(
    shopping_lists_page: ShoppingListsPage, shopping_list: list[list[str]]
) -> None:
    """Тест проверки списка покупок."""
    shopping_list_page = shopping_lists_page.open_shopping_list("birthday party")
    with allure.step("Проверка соответствия названия списка для покупок"):
        assert shopping_list_page.get_list_name() == "birthday party"
    cart_entries = shopping_list_page.get_all_entries_content()
    assert_lists_equal(shopping_list, cart_entries, "Ошибка проверки списка покупок")


@allure.title("Проверка списка покупок пользователя с использованием orm")
@pytest.mark.ui
@pytest.mark.shopping_list
@pytest.mark.parametrize("shopping_list_orm", ["friday's lunch"], indirect=True)
def test_user_shopping_orm(
    shopping_lists_page: ShoppingListsPage, shopping_list_orm: list[list[str]]
) -> None:
    """Тест проверки списка покупок."""
    shopping_list_page = shopping_lists_page.open_shopping_list("friday's lunch")
    assert shopping_list_page.get_list_name() == "friday's lunch"
    cart_entries = shopping_list_page.get_all_entries_content()
    assert_lists_equal(shopping_list_orm, cart_entries, "Ошибка проверки списка покупок")
