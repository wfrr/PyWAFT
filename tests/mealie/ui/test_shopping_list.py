"""Модуль тестов списка покупок."""

import allure
import pytest

from library.mealie.assertions.common import assert_ints_equal, assert_strings_equal
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
    entry_notes = shopping_list_page.get_all_entry_notes_text()
    assert_ints_equal(
        len(shopping_list), len(entry_notes), "Ошибка проверки длины списка покупок"
    )
    for exp_entry, entry_note in zip(shopping_list, entry_notes, strict=True):
        assert_strings_equal(exp_entry[3], entry_note, "Ошибка проверки списка покупок")


@allure.title("Проверка списка покупок пользователя с использованием orm")
@pytest.mark.ui
@pytest.mark.shopping_list
@pytest.mark.parametrize("shopping_list_orm", ["friday's lunch"], indirect=True)
def test_user_shopping_orm(
    shopping_lists_page: ShoppingListsPage, shopping_list_orm: list[list[str]]
) -> None:
    """Тест проверки списка покупок."""
    shopping_list_page = shopping_lists_page.open_shopping_list("friday's lunch")
    with allure.step("Проверка соответствия названия списка для покупок"):
        assert shopping_list_page.get_list_name() == "friday's lunch"
    entry_notes = shopping_list_page.get_all_entry_notes_text()
    assert_ints_equal(
        len(shopping_list_orm), len(entry_notes), "Ошибка проверки длины списка покупок"
    )
    for exp_entry, entry_note in zip(shopping_list_orm, entry_notes, strict=True):
        assert_strings_equal(exp_entry[3], entry_note, "Ошибка проверки списка покупок")
