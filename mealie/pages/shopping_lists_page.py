"""Модуль страницы списков покупок пользователя."""

from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage


class ShoppingListsPage(BasePage):
    """Класс страницы списков покупок пользователя."""

    def __init__(self, driver: Chrome | Firefox | Edge) -> None:
        """Инициализация класса страницы списка покупок пользователя."""
        super().__init__(driver)
        self.driver = driver
        self.timeout = 15
        WebDriverWait(self.driver, self.timeout).until(
            ec.title_is('Shopping List'),
            message='Ошибка перехода на домащнюю страницу',
        )
