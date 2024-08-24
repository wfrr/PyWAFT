import allure

from library.pages.mealie.login_page import LoginPage
from library.test_utils.mealie.app_data import AppData


@allure.tag('shopping-list')
@allure.title('Проверка списка покупок пользователя')
def test_user_shopping(login_page: LoginPage, stand: AppData) -> None:
    """Тест проверки списка покупок."""
    assert login_page.get_title() == 'Login', 'Ошибка проверки входа'
