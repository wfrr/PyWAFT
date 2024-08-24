from typing import Annotated, Type, TypeVar, get_origin
from selenium.webdriver.remote.webdriver import WebDriver

T = TypeVar('T')


def page_factory(driver: WebDriver, page_class: Type[T]) -> Type:
    """
    Фабрика страниц POM

    Пример класса страницы:

       class SomePage:
           menu_element = Annotated[WebElement, By.XPATH, '//*[@href="somelink"]]
    """
    page_object = page_class(driver)
    for field_name, field_value in page_class.__dict__.items():
        if get_origin(field_value) is Annotated:
            # ищем элементы по локаторам как атрибутам класса
            loc_strat, loc_value = field_value.__metadata__
            field_value = driver.find_element(by=loc_strat, value=loc_value)
            page_object.__dict__[field_name] = field_value
    return page_object
