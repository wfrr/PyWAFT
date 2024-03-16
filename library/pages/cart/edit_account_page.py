"""Модуль страницы редактирования данных учетной записи"""

import allure
from selenium.webdriver.common.by import By

from library.pages.cart.base_page import BasePage


class EditAccountPage(BasePage):
    """Класс страницы редактирования данных учетной записи"""

    _first_name_locator = (By.ID, 'input-firstname')
    _last_name_locator = (By.ID, 'input-lastname')
    _email_locator = (By.ID, 'input-email')
    _continue_btn_locator = (By.CSS_SELECTOR, 'button.btn-primary')

    def get_first_name(self) -> str:
        """
        Получения значения First Name

        :returns str: установленное имя
        """
        with allure.step('Получения значения First Name'):
            return self.get_element_text(self._first_name_locator, is_attribute=True)

    def get_last_name(self) -> str:
        """
        Получения значения Last Name

        :returns str: установленная фамилия
        """
        with allure.step('Получения значения Last Name'):
            return self.get_element_text(self._last_name_locator, is_attribute=True)

    def get_email(self) -> str:
        """
        Получения значения E-Mail

        :returns str: установленный email
        """
        with allure.step('Получения значения E-Mail'):
            return self.get_element_text(self._email_locator, is_attribute=True)

    def change_first_name(self, name: str) -> None:
        """
        Установка значения First Name

        :param str name: новое имя
        """
        with allure.step(f'Установка значения First Name: {name}'):
            self.do_send_keys(self._first_name_locator, name)

    def change_last_name(self, name: str) -> None:
        """
        Установка значения Last Name

        :param str name: новая фамилия
        """
        with allure.step(f'Установка значения Last Name: {name}'):
            self.do_send_keys(self._last_name_locator, name)

    def change_email(self, email: str) -> None:
        """
        Установка значения E-Mail

        :param str email: новый email
        """
        with allure.step(f'Установка значения E-Mail: {email}'):
            self.do_send_keys(self._last_name_locator, email)

    def save_changes(self) -> None:
        """Сохрание изменений нажатием кнопки 'Continue'"""
        with allure.step('Сохранение изменений нажатием кнопки "Continue"'):
            url = self.driver.current_url
            self.do_click(self._continue_btn_locator)
            self.wait_url_changes(url)
