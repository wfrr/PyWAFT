"""Модуль домашней страницы пользователя"""

from typing import Union
from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from .base_page import BasePage


class HomePage(BasePage):
    """Класс домашней страницы пользователя"""

    def __init__(self, driver: Union[Chrome, Firefox, Edge]) -> None:
        super().__init__(driver)
        self.driver = driver
        self.timeout = 15
        WebDriverWait(self.driver, self.timeout).until(
            ec.title_is('Mealie'), message='Ошибка перехода на домащнюю страницу')
