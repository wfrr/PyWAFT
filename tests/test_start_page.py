import allure
import pytest

from config.config import TestData
from library.pages.main_page import MainPage
from library.pages.login_page import LoginPage
from library.pages.account_page import AccountPage
from library.test_utils.base_test import BasicTest


class TestStartPage(BasicTest):

    @pytest.fixture(scope='class')
    @allure.title('Открытие главной страницы')
    def main_page(self):
        yield MainPage(self.driver, TestData.URL)

    @pytest.fixture
    @allure.title('Переход на страницу логина')
    def login_page(self, main_page):
        main_page.open_account_options()
        main_page.select_login()
        yield LoginPage(self.driver)

    @allure.title('Проверка стартовой страницы')
    def test_start_page(self, main_page):
        title = main_page.get_title()
        self.assert_strings_equal(
            value1=title, value2="Your Store", msg="Заголовки не совпадают"
        )

    @allure.title('Проверка входа в личный кабинет обычным пользователем')
    def test_user_logon(self, login_page):
        login_page.fill_login(TestData.CUSTOMER_EMAIL)
        login_page.fill_password(TestData.CUSTOMER_PASSWORD)
        login_page.do_login()
        account_page = AccountPage(self.driver)
        self.assert_strings_equal(value1=account_page.get_title(), value2='My Account',
                                  msg='Ошибка проверки входа')
