import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage


class AccountPage(BasePage):

    _icon_locator = (By.ID, 'logo')

    def get_title(self) -> str:
        """Получение заголовка страницы"""
        with allure.step('Получение заголовка страницы'):
            self.wait_visibility_of_element_located(self._icon_locator)
            return super().get_title()
