"""Модуль страницы списков покупок пользователя."""

import allure
from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from library.core.page_factory import init_class_elements

from .base_page import BasePage
from .shopping_list_page import ShoppingListPage


class ShoppingListsPage(BasePage):
    """Класс страницы списков покупок пользователя."""

    def __init__(self, driver: Chrome | Firefox | Edge) -> None:
        """Инициализация класса страницы списков покупок пользователя."""
        super().__init__(driver)
        self.driver = driver
        self.timeout = 15
        WebDriverWait(self.driver, self.timeout).until(
            ec.title_is("Shopping List"),
            message="Ошибка перехода на домащнюю страницу",
        )

    def open_shopping_list(self, name: str) -> ShoppingListPage:
        """Открытие списка покупок по названию.

        :param name str: название списка покупок
        :return ShoppingListPage: ссылка на объект списка покупок пользователя
        """
        with allure.step("Открытие списка покупок по названию"):
            url = self.driver.current_url
            shopping_list_name_locator = (
                By.XPATH,
                f'''//*[contains(@class,"v-card-title")]/span[contains(text(),"{name}")]''',
            )
            self.driver.find_element(*shopping_list_name_locator).click()
            WebDriverWait(self.driver, 10).until(ec.url_changes(url))
            return init_class_elements(self.driver, ShoppingListPage)
