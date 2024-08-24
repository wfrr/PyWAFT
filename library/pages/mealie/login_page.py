"""Модуль страницы входа."""

from typing import Annotated

import allure
from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from library.test_utils.page_factory import page_factory

from .base_page import BasePage
from .home_page import HomePage


class LoginPage(BasePage):
    """Класс страницы входа."""

    _login_field = Annotated[WebElement, By.NAME, 'login']
    _password_field = Annotated[WebElement, By.ID, 'password']
    _login_btn = Annotated[WebElement, By.CSS_SELECTOR, '.v-form button[type=submit]']

    def __init__(self, driver: Chrome | Firefox | Edge) -> None:
        super().__init__(driver)
        self.driver = driver
        self.timeout = 15
        WebDriverWait(self.driver, self.timeout).until(
            ec.title_is('Login'),
            message='Ошибка перехода на страницу входа',
        )

    def fill_login(self, login: str) -> None:
        """Заполнение поля 'E-Mail or Username'.

        :param str login: логин пользователя
        """
        with allure.step(f'Заполнение поля "E-Mail or Username" текстом: {login}'):
            self._login_field.clear()
            self._login_field.send_keys(login)

    def fill_password(self, passwd: str) -> None:
        """Заполнение поля 'Password'.

        :param str passwd: пароль пользователя
        """
        with allure.step('Заполнение поля "Password"'):
            self._password_field.clear()
            self._password_field.send_keys(passwd)

    def do_login(self) -> None:
        """Нажатие кнопки 'Login'."""
        with allure.step('Нажатие кнопки "Login"'):
            url = self.driver.current_url
            WebDriverWait(self.driver, self.timeout).until(ec.element_to_be_clickable(self._login_btn)).click()
            WebDriverWait(self.driver, self.timeout).until(ec.url_changes(url))

    def login_user(self, username: str, passwd: str) -> HomePage:
        """Вход пользователя.

        :param str username: имя пользователя
        :param str passwd: пароль пользователя
        :return HomePage: ссылка на объект домашней страницы пользователя
        """
        with allure.step(f'Вход покупателя {username}'):
            self.fill_login(username)
            self.fill_password(passwd)
            self.do_login()
            return page_factory(self.driver, HomePage)
