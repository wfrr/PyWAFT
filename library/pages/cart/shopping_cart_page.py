"""Модуль страницы корзины покупателя"""

import allure
from selenium.webdriver.common.by import By

from library.pages.cart.base_page import BasePage


class ShoppingCartPage(BasePage):
    """Класс страницы корзины покупателя"""

    __product_name_locator = (
        By.CSS_SELECTOR, '#checkout-cart tbody td:nth-of-type(2) a')
    __model_locator = (
        By.CSS_SELECTOR, '#checkout-cart tbody td:nth-of-type(3)')
    __quantity_locator = (
        By.CSS_SELECTOR, '#checkout-cart tbody td:nth-of-type(4) input[type=text]')

    def get_n_entries(self, entry_num: int = 1) -> list[dict[str, str]]:
        """
        Получение N записей из корзины

        :param int entry_num: количество записей для получния
        :return list: список полученных данных
        """
        with allure.step(f'Получение {entry_num} записей из корзины'):
            entries = []
            for name, model, quantity in zip(self.get_all_elements_text(self.__product_name_locator),
                                             self.get_all_elements_text(
                                                 self.__model_locator),
                                             self.get_all_elements_text(self.__quantity_locator,
                                                                        is_attribute=True)
                                             ):
                entries.append(
                    {'name': name, 'model': model, 'quantity': quantity})
            return entries[:entry_num]
