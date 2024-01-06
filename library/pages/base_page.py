from typing import Optional, Tuple

import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def do_click(self, locator: Tuple[str, str]) -> None:
        """
        Нажатие на элемент

        :param Tuple[str, str] locator: локатор элемента
        """
        with allure.step(f'Нажатие на элемент по локатору {locator}'):
            self.wait_element_to_be_clickable(locator=locator).click()

    def do_send_keys(self, locator: Tuple[str, str], text: str) -> None:
        """
        Отправка последовательности символов в элемент

        :param Tuple[str, str] locator: локатор элемента
        :param str text: текст для передачи в элемент
        """
        with allure.step(f'Отправка последовательности символов {text} в элемент по локатору {locator}'):
            el = self.wait_visibility_of_element_located(locator=locator)
            el.clear()
            el.send_keys(text)

    def do_send_keys_no_log(self, locator: Tuple[str, str], text: str) -> None:
        """
        Отправка последовательности символов в элемент без логирования текста

        :param Tuple[str, str] locator: локатор элемента
        :param str text: текст для передачи в элемент
        """
        with allure.step(f'Отправка последовательности символов в элемент по локатору {locator}'):
            el = self.wait_visibility_of_element_located(locator=locator)
            el.clear()
            el.send_keys(text)

    def get_title(self) -> str:
        """
        Получение заголовка страницы

        :returns str: заголовок страницы
        """
        with allure.step('Получение заголовка страницы'):
            return self.driver.title

    def scroll_to_bottom(self) -> None:
        """Прокручивание страницы вниз до конца"""
        with allure.step('Прокручивание страницы вниз до конца'):
            # TODO: скрипт для прокручивания вниз до конца страницы
            self.driver.execute_script('')

    def get_element_text(self, locator: Tuple[str, str], is_attribute: Optional[bool] = False) -> str:
        """
        Получение текста элемента

        :param Tuple[str, str] locator: локатор элемента
        :param Optional[bool] is_attribute: флаг получения текста из атрибута элемента
        :returns str: текст элемента
        """
        with allure.step(f'Получение текста элемента по локатору {locator}'):
            el = self.wait_visibility_of_element_located(locator=locator)
            if is_attribute:
                return el.get_property('value')
            return el.text

    def get_all_elements_text(self, locator: Tuple[str, str], is_attribute: Optional[bool] = False) -> list[str]:
        """
        Получение текста всех элементов

        :param Tuple[str, str] locator: локатор элемента
        :param Optional[bool] is_attribute: флаг получения текста из атрибута элемента
        :returns list: список текстов элементов
        """
        with allure.step(f'Получение текстов всех элементов по локатору {locator}'):
            elements = []
            for el in self.wait_visibility_of_all_elements_located(locator=locator):
                if is_attribute:
                    elements.append(el.get_property('value'))
                    continue
                elements.append(el.text)
            return elements

    def wait_visibility_of_element_located(self, locator: Tuple[str, str], timeout: Optional[int] = None) -> WebElement:
        """
        Ожидание видимости элемента по локатору

        :param Tuple[str, str] locator: локатор элемента
        :param Optional[int] timeout: время ожидания нахождения элемента
        :returns WebElement: найденный элемент
        """
        with allure.step(f'Ожидание видимости элемента по локатору {locator}'):
            timeout = timeout or self.timeout
            return WebDriverWait(self.driver, timeout, ignored_exceptions=[]).until(
                ec.visibility_of_element_located(locator))

    def wait_visibility_of_all_elements_located(
            self, locator: Tuple[str, str], timeout: Optional[int] = None
    ) -> list[WebElement]:
        """
        Ожидание видимости всех элементов по локатору

        :param Tuple[str, str] locator: локатор элемента
        :param Optional[int] timeout: время ожидания нахождения элемента
        :returns list: список найденных элементов
        """
        with allure.step(f'Ожидание видимости всех элементов по локатору {locator}'):
            timeout = timeout or self.timeout
            return WebDriverWait(self.driver, timeout, ignored_exceptions=[]).until(
                ec.visibility_of_all_elements_located(locator))

    def wait_element_to_be_clickable(self, locator: Tuple[str, str], timeout: Optional[int] = None) -> WebElement:
        """
        Ожидание видимости элемента по локатору

        :param Tuple[str, str] locator: локатор элемента
        :param Optional[int] timeout: время ожидания нахождения элемента
        :returns WebElement: найденный элемент
        """
        with allure.step(f'Ожидание видимости элемента по локатору {locator}'):
            timeout = timeout or self.timeout
            return WebDriverWait(self.driver, timeout, ignored_exceptions=[]).until(ec.element_to_be_clickable(locator))

    def wait_url_changes(self, url: str, timeout: Optional[int] = None) -> bool:
        """
        Ожидание изменения URL

        :param str url: текущий url
        :param Optional[int] timeout: время ожидания нахождения элемента
        :returns bool: булево значение, обозначающее результат изменения url
        """
        with allure.step('Ожидание изменения URL'):
            timeout = timeout or self.timeout
            return WebDriverWait(self.driver, timeout, ignored_exceptions=[]).until(ec.url_changes(url))
