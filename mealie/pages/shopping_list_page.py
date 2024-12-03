"""Модуль страницы списка покупок пользователя."""

from typing import Annotated

from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage


class Entry:
    """Класс элемента списка покупок."""

    def __init__(self, root: WebElement) -> None:
        """Инициализация класса элементов списков покупок пользователя."""
        self._root = root

    def get_note(self) -> str:
        """Получения текста записи."""
        return self._root.find_element(By.XPATH, './/p').text


class ShoppingListPage(BasePage):
    """Класс страницы списка покупок пользователя."""

    _shopping_list_headline: Annotated[WebElement, By.CSS_SELECTOR, 'h2.headline']

    def __init__(self, driver: Chrome | Firefox | Edge) -> None:
        """Инициализация класса страницы списка покупок пользователя."""
        super().__init__(driver)
        self.driver = driver
        self.timeout = 15
        WebDriverWait(self.driver, self.timeout).until(
            ec.title_is('Shopping List'),
            message='Ошибка перехода на страницу списка покупок',
        )

    def get_list_name(self) -> str:
        """Получение названия списка для покупок.

        :returns: название списка покупок
        """
        return self._shopping_list_headline.text

    def get_all_entry_notes(self) -> list[Entry]:
        """Получение списка всех записей.

        :returns: список элементов в списке покупок
        """
        _shopping_list_entry = self.driver.find_elements(By.CSS_SELECTOR, 'section div.v-lazy')
        return [Entry(el) for el in _shopping_list_entry]

    def get_all_entry_notes_text(self) -> list[str]:
        """Получение списка текстов всех записей.

        :returns: список текстов в элементах списка покупок
        """
        return [e.get_note() for e in self.get_all_entry_notes()]
