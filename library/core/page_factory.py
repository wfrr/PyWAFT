"""Модуль фабрики страниц тестируемого приложедния.

Пример класса страницы:

    class SomePage:
        menu_element: Annotated[WebElement, By.XPATH, '//*[@href="somelink"]]

        def click_menu():
            self.menu_element.click()
"""

from typing import TypeVar, get_type_hints

from selenium.webdriver.remote.webdriver import WebDriver

PageType = TypeVar("PageType")


def init_class_elements(driver: WebDriver, page_type: type[PageType]) -> PageType:
    """Инициализация элементов страницы класса страницы POM.

    :param WebDriver driver: веб-драйвер для инициализации страницы
    :param type[T] page_type: класс страницы для инициализации
    :returns T: объект инициализированной страницы
    """
    obj = page_type(driver)
    init_object_elements(driver, obj)
    return obj


def init_object_elements(driver: WebDriver, page_obj: PageType) -> None:
    """Инициализация элементов страницы объекта страницы POM.

    :param WebDriver driver: веб-драйвер для инициализации страницы
    :param T page_obj: объект страницы
    """
    if not getattr(page_obj, "__annotations__", None):
        return
    for attr_name, typedata in get_type_hints(page_obj, include_extras=True).items():
        element = driver.find_element(*typedata.__metadata__)
        setattr(page_obj, attr_name, element)
