import allure
import pytest

from library.pages.admin_login_page import AdminLoginPage
from library.pages.main_page import MainPage
from library.test_utils.base import assert_strings_equal


@allure.tag('smoke')
@allure.title('Проверка стартовой страницы')
@pytest.mark.smoke
def test_main_page(main_page: MainPage) -> None:
    title = main_page.get_title()
    assert_strings_equal(value1=title, value2='Your Store', msg='Заголовки не совпадают')


@allure.tag('smoke')
@allure.title('Проверка страницы входа администратора')
@pytest.mark.smoke
def test_admin_login_page(admin_login_page: AdminLoginPage) -> None:
    title = admin_login_page.get_title()
    assert_strings_equal(value1=title, value2='Administration', msg='Заголовки не совпадают')
