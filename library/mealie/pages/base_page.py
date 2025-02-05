"""Модуль базовый страницы POM Mealie."""

import allure
from selenium.webdriver import Chrome, Edge, Firefox


class BasePage:
    """Базовая страница POM."""

    def __init__(self, driver: Chrome | Firefox | Edge) -> None:
        """Инициализация класса базовой страницы."""
        self.driver = driver
        self.timeout = 10

    def get_title(self) -> str:
        """Получение заголовка страницы.

        :returns str: заголовок страницы
        """
        with allure.step("Получение заголовка страницы"):
            return self.driver.title

    def scroll_to_bottom(self) -> None:
        """Прокручивание стриницы вниз."""
        with allure.step("Прокручивание стриницы вниз"):
            self.driver.execute("window.scrollTo(0, document.body.scrollHeight);")
