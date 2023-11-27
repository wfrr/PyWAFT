import allure

from library.test_utils.base_test import assert_strings_equal


@allure.title('Проверка стартовой страницы')
def test_main_page(main_page):
    title = main_page.get_title()
    assert_strings_equal( value1=title, value2='Your Store', msg='Заголовки не совпадают')
