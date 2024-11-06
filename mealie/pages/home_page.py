"""Модуль домашней страницы пользователя."""

from typing import Annotated

import allure
from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from core.page_factory import init_class_elements

from .base_page import BasePage
from .shopping_lists_page import ShoppingListsPage


class HomePage(BasePage):
    """Класс домашней страницы пользователя."""

    _side_menu_btn: Annotated[WebElement, By.CSS_SELECTOR, '.v-toolbar__content > button:nth-child(1)']
    _side_menu_profile_link: Annotated[WebElement, By.CSS_SELECTOR, 'nav a[href="/user/profile"]']
    _shopping_lists_menu_entry: Annotated[WebElement, By.CSS_SELECTOR, 'a[href="/shopping-lists"]']

    def __init__(self, driver: Chrome | Firefox | Edge) -> None:
        """Инициализация класса домашней страницы."""
        super().__init__(driver)
        self.driver = driver
        self.timeout = 15
        WebDriverWait(self.driver, self.timeout).until(
            ec.title_is('Mealie'),
            message='Ошибка перехода на домащнюю страницу',
        )

    def ensure_side_menu_open(self) -> None:
        """Открытие боковой панели меню, если она закрыта."""
        with allure.step('Открытие боковой панели меню'):
            if not self._side_menu_profile_link.is_displayed():
                self._side_menu_btn.click()
                WebDriverWait(self.driver, self.timeout).until(ec.element_to_be_clickable(self._side_menu_profile_link))

    def open_shopping_lists(self) -> None:
        """Открытие страницы Shopping Lists."""
        with allure.step('Открытие страницы Shopping Lists'):
            self.ensure_side_menu_open()
            WebDriverWait(self.driver, self.timeout).until(
                ec.element_to_be_clickable(self._shopping_lists_menu_entry)).click()
            return init_class_elements(self.driver, ShoppingListsPage)
