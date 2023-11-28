from typing import Union

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):

    _login_field_locator = (By.CSS_SELECTOR, '#form-login input[type=text]')
    _password_field_locator = (By.CSS_SELECTOR, '#form-login input[type=password]')
    _login_btn_locator = (By.CSS_SELECTOR, '#form-login button[type=submit]')

    def __init__(self, driver: Union[WebDriver]):
        super().__init__(driver)
        self.driver = driver
        self.timeout = 15

    def fill_login(self, login: str) -> None:
        """
        Заполнение поля 'E-Mail Address'
        
        :param str login: логин пользователя
        """
        with allure.step(f'Заполнение поля "E-Mail Address" текстом: {login}'):
            self.do_send_keys(self._login_field_locator, login)

    def fill_password(self, passwd: str) -> None:
        """
        Заполнение поля 'Password'
        
        :param str passwd: пароль пользователя
        """
        with allure.step('Заполнение поля "Password"'):
            self.do_send_keys_no_log(self._password_field_locator, passwd)

    def do_login(self) -> None:
        """Нажатие кнопки 'Login'"""
        with allure.step('Нажатие кнопки "Login"'):
            url = self.driver.current_url
            self.do_click(self._login_btn_locator)
            self.wait_url_changes(url)
