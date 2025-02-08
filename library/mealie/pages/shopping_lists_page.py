"""Модуль страницы списков покупок пользователя."""

from typing import Annotated

import allure
from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from library.core.page_factory import init_class_elements

from .base_page import BasePage
from .shopping_list_page import ShoppingListPage


class ShoppingList:
    """Класс элемента списков покупок."""

    def __init__(self, root: WebElement) -> None:
        """Инициализация класса элементов списков покупок пользователя."""
        self._root = root

    def get_name(self) -> str:
        """Получение названия списка для покупок."""
        return self._root.find_element(By.XPATH, "./div").text

    def open(self) -> None:
        """Открытие списка покупок."""
        self._root.find_element(By.XPATH, "./div").click()


class ShoppingListsPage(BasePage):
    """Класс страницы списков покупок пользователя."""

    _shopping_lists_headline: Annotated[WebElement, By.CSS_SELECTOR, "h2.headline"]

    def __init__(self, driver: Chrome | Firefox | Edge) -> None:
        """Инициализация класса страницы списков покупок пользователя."""
        super().__init__(driver)
        self.driver = driver
        self.timeout = 15
        WebDriverWait(self.driver, self.timeout).until(
            ec.title_is("Shopping List"),
            message="Ошибка перехода на домащнюю страницу",
        )

    def shopping_lists(self) -> list[ShoppingList]:
        """Получение списка списков для покупок.

        :returns: список объектов элементов списка покупок
        """
        with allure.step("Получение списка списков для покупок"):
            _shopping_lists = self.driver.find_elements(
                By.CSS_SELECTOR, "div.container:nth-child(1) > section .v-card"
            )
            return [ShoppingList(el) for el in _shopping_lists]

    def open_shopping_list(self, name: str) -> ShoppingListPage:
        """Открытие списка покупок по названию.

        :param name str: название списка покупок
        :return ShoppingListPage: ссылка на объект списка покупок пользователя
        """
        with allure.step("Открытие списка покупок по названию"):
            next(filter(lambda e: e.get_name() == name, self.shopping_lists())).open()
            return init_class_elements(self.driver, ShoppingListPage)
