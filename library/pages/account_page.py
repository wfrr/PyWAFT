from typing import Union

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from .base_page import BasePage


class AccountPage(BasePage):

    _icon_locator = (By.ID, 'logo')
    _edit_account_page_locator = (By.CSS_SELECTOR, '.list-group-item:nth-child(2)')
    _success_msg_locator = (By.CLASS_NAME, 'alert-success')
    __cart_btn_locator = (By.CSS_SELECTOR, 'a[title="Shopping Cart"]')

    def __init__(self, driver: Union[WebDriver]):
        super().__init__(driver)
        self.driver = driver
        self.timeout = 15

    def get_title(self) -> str:
        """Получение заголовка страницы"""
        with allure.step('Получение заголовка страницы'):
            self.wait_visibility_of_element_located(self._icon_locator)
            return super().get_title()

    def edit_account_page(self) -> None:
        """Переход на страницу редактирования персональных данных клиента"""
        with allure.step('Получение заголовка страницы'):
            self.do_click(self._edit_account_page_locator)

    def get_success_msg(self) -> str:
        """Получение сообщения об успешной операции"""
        with allure.step('Получение сообщения об успешной операции'):
            return self.get_element_text(self._success_msg_locator)

    def open_shopping_cart(self) -> None:
        """Открытие корзины"""
        with allure.step('Открытие корзины'):
            url = self.driver.current_url
            self.do_click(self.__cart_btn_locator)
            self.wait_url_changes(url)
