from typing import Union

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from library.pages.base_page import BasePage


class AdminLoginPage(BasePage):

    _icon_locator = (By.CSS_SELECTOR, '#header a.navbar-brand img')

    def __init__(self, driver: Union[WebDriver]):
        super().__init__(driver)
        self.driver = driver
        self.timeout = 15

    def get_title(self) -> str:
        """Получение заголовка страницы"""
        with allure.step('Получение заголовка страницы'):
            self.wait_visibility_of_element_located(self._icon_locator)
            return self.driver.title
