"""Модуль фабрики страниц тестируемого приложедния.

Пример класса страницы:

    class SomePage:
        menu_element: Annotated[WebElement, By.XPATH, '//*[@href="somelink"]]

        def click_menu():
            self.menu_element.click()
"""

from typing import TypeVar, get_type_hints

from selenium.webdriver.remote.webdriver import WebDriver

T = TypeVar('T')


def init_class_elements(driver: WebDriver, page: type[T]) -> T:
    """Инициализация элементов страницы класса страницы POM."""
    obj = page(driver)
    init_object_elements(driver, obj)
    return obj


def init_object_elements(driver: WebDriver, page_obj: T) -> None:
    """Инициализация элементов страницы объекта страницы POM."""
    for attr_name, typedata in get_type_hints(page_obj, include_extras=True).items():
        element = driver.find_element(*typedata.__metadata__)
        setattr(page_obj, attr_name, element)
