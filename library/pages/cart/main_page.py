"""Модуль главной страницы"""

from typing import Union

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    """Класс главной страницы"""

    _icon_locator = (By.ID, 'logo')
    _my_account_dropdown_locator = (
        By.CSS_SELECTOR, '.nav.float-end .dropdown span')
    _register_dropdown_option_locator = (
        By.CSS_SELECTOR, '.nav.float-end .dropdown-menu li:nth-child(1) a')
    _login_dropdown_option_locator = (
        By.CSS_SELECTOR, '.nav.float-end .dropdown-menu li:nth-child(2) a')

    def __init__(self, driver: Union[WebDriver]):
        super().__init__(driver)
        self.driver = driver
        self.timeout = 15

    def get_title(self) -> str:
        """Получение заголовка страницы"""
        with allure.step('Получение заголовка страницы'):
            self.wait_visibility_of_element_located(self._icon_locator)
            return self.driver.title

    def open_account_options(self) -> None:
        """Открытие меню 'My account'"""
        with allure.step('Открытие меню "My account"'):
            self.do_click(self._my_account_dropdown_locator)
            self.wait_visibility_of_element_located(
                self._register_dropdown_option_locator)

    def select_login(self) -> None:
        """Выбор 'Login' в выпадающем меню"""
        with allure.step('Выбор "Login" в выпадающем меню'):
            url = self.driver.current_url
            self.do_click(self._login_dropdown_option_locator)
            self.wait_url_changes(url)
