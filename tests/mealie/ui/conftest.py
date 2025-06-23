"""Фикстуры автотестов Mealie."""

from collections.abc import Callable, Generator
from platform import platform

import allure
import pytest
from _pytest.fixtures import SubRequest
from selenium.webdriver import Chrome, Edge, Firefox

from library.core.app_data import AppData
from library.core.browser import init_chrome, init_edge, init_firefox
from library.core.browser_data import BrowserData
from library.core.page_factory import init_object_elements
from library.mealie.database.queries import (
    select_shopping_list_by_name,
    select_shopping_list_by_name_orm,
)
from library.mealie.pages.home_page import HomePage
from library.mealie.pages.login_page import LoginPage
from library.mealie.pages.shopping_lists_page import ShoppingListsPage


@pytest.fixture(scope="session", autouse=True)
@allure.title("Запись переменных окружения")
def environment(
    add_allure_env_property: Callable, stand: AppData, browser_data: BrowserData
) -> None:
    """Наполнение allure-отчета требуемыми переменными окружения."""
    add_allure_env_property("ENV", stand.app["env"])
    add_allure_env_property("Browser", browser_data.name)
    add_allure_env_property("BrowserVersion", browser_data.version)
    add_allure_env_property("OS", platform())


@pytest.fixture
@allure.title("Инициализация веб драйвера")
def driver(
    browser_data: BrowserData,
) -> Generator[Chrome | Firefox | Edge, None, None]:
    """Инициализация веб-драйвера."""
    init_browser = {"chrome": init_chrome, "firefox": init_firefox, "edge": init_edge}
    if browser_data.name not in init_browser.keys():
        raise NotImplementedError(f"{browser_data.name} не поддерживается")
    _driver = init_browser[browser_data.name](browser_data)
    yield _driver
    _driver.quit()


@pytest.fixture
@allure.title("Переход на страницу логина")
def login_page(driver: Chrome | Firefox | Edge, stand: AppData) -> LoginPage:
    """Открытие страницы входа пользователя."""
    driver.get(stand.app["url"])
    page = LoginPage(driver)
    init_object_elements(driver, page)
    return page


@pytest.fixture
@allure.title("Домашняя страница пользователя")
def home_page(stand: AppData, login_page: LoginPage) -> HomePage:
    """Открытие домашней страницы пользователя."""
    return login_page.login_user(
        stand.users["regular"]["username"], stand.users["regular"]["password"]
    )


@pytest.fixture
@allure.title("Cтраница списка покупок пользователя")
def shopping_lists_page(home_page: HomePage) -> ShoppingListsPage:
    """Открытие страницы списков покупок пользователя."""
    return home_page.open_shopping_lists()


@pytest.fixture
@allure.title("Получение списка покупок по названию")
def shopping_list(stand: AppData, request: SubRequest) -> list[list[str]]:
    """Получение списка покупок по названию."""
    return select_shopping_list_by_name(
        stand.db, request.param, stand.users["regular"]["username"]
    )


@pytest.fixture
@allure.title("Получение списка покупок по названию")
def shopping_list_orm(stand: AppData, request: SubRequest) -> list[list[str]]:
    """Получение списка покупок по названию с использованием ORM."""
    return select_shopping_list_by_name_orm(
        stand.db, request.param, stand.users["regular"]["username"]
    )
