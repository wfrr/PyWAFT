import allure

from library.pages.main_page import MainPage
from library.test_utils.base import assert_strings_equal


@allure.tag('smoke')
@allure.title('Проверка стартовой страницы')
def test_main_page(main_page: MainPage) -> None:
    title = main_page.get_title()
    assert_strings_equal(value1=title, value2='Your Store', msg='Заголовки не совпадают')
