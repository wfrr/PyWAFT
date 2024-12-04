import allure
import pytest

from mealie.pages.shopping_lists_page import ShoppingListsPage


@allure.tag('shopping-list')
@allure.title('Проверка списка покупок пользователя')
@pytest.mark.parametrize('shopping_list', ['birthday party'], indirect=True)
@pytest.mark.ui
@pytest.mark.shopping_list
def test_user_shopping(shopping_lists_page: ShoppingListsPage, shopping_list: list[list[str]]) -> None:
    """Тест проверки списка покупок."""
    shopping_list_page = shopping_lists_page.open_shopping_list('birthday party')
    assert shopping_list_page.get_list_name() == 'birthday party'
    entry_notes = shopping_list_page.get_all_entry_notes_text()
    assert len(shopping_list) == len(entry_notes)
    for exp_entry, entry_note in zip(shopping_list, entry_notes, strict=True):
        assert exp_entry[3] == entry_note


@allure.tag('shopping-list')
@allure.title('Проверка списка покупок пользователя с использованием orm')
@pytest.mark.ui
@pytest.mark.shopping_list
@pytest.mark.parametrize('shopping_list_orm', ["friday's lunch"], indirect=True)
def test_user_shopping_orm(shopping_lists_page: ShoppingListsPage, shopping_list_orm: list[list[str]]) -> None:
    """Тест проверки списка покупок."""
    shopping_list_page = shopping_lists_page.open_shopping_list("friday's lunch")
    assert shopping_list_page.get_list_name() == "friday's lunch"
    entry_notes = shopping_list_page.get_all_entry_notes_text()
    assert len(shopping_list_orm) == len(entry_notes)
    for exp_entry, entry_note in zip(shopping_list_orm, entry_notes, strict=True):
        assert exp_entry[0] == entry_note
