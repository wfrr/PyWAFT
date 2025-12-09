"""Модуль фабрики страниц тестируемого приложедния.

Пример класса страницы:

    class SomePage:
        menu_element: Annotated[WebElement, By.XPATH, '//*[@href="somelink"]]

        def click_menu():
            self.menu_element.click()
"""

from typing import Protocol, TypeVar, get_type_hints

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

PageType = TypeVar("PageType", covariant=True)


class Constructor(Protocol[PageType]):
    def __call__(self, *args, **kwargs) -> PageType: ...


def init_class_elements(driver: WebDriver, page_type: Constructor[PageType]) -> PageType:
    """Инициализация элементов страницы класса страницы POM.

    :param WebDriver driver: веб-драйвер для инициализации страницы
    :param type[T] page_type: класс страницы для инициализации
    :returns T: объект инициализированной страницы
    """
    obj = page_type(driver)
    init_object_elements(driver, obj)
    return obj


def init_object_elements(driver: WebDriver, page_obj: object) -> None:
    """Инициализация элементов страницы объекта страницы POM.

    :param WebDriver driver: веб-драйвер для инициализации страницы
    :param T page_obj: объект страницы
    """
    if not getattr(page_obj, "__annotations__", None):
        return
    for attr_name, typedata in get_type_hints(page_obj, include_extras=True).items():
        element = WebDriverWait(driver, 10).until(
            ec.any_of(
                ec.presence_of_element_located(typedata.__metadata__),
                ec.visibility_of_element_located(typedata.__metadata__),
                ec.element_to_be_clickable(typedata.__metadata__),
            ),
            message="Ошибка перехода на домащнюю страницу",
        )
        setattr(page_obj, attr_name, element)
