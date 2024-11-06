import allure
import pytest

from mealie.pages.shopping_lists_page import ShoppingListsPage


@allure.tag('shopping-list')
@allure.title('Проверка списка покупок пользователя')
@pytest.mark.parametrize('shopping_list', 'birthday party', indirect=True)
def test_user_shopping(shopping_lists_page: ShoppingListsPage, shopping_list: list[list[str]]) -> None:
    """Тест проверки списка покупок."""
    shopping_lists_page.open_shopping_list()
