from http import HTTPStatus

import allure
import pytest

from library.api.api_client import ApiClient
from library.assertions.api import assert_schema, assert_status_code
from library.mealie.api.actions.about_app_info import get_app_info, get_app_startup_info
from library.mealie.api.models import APP_ABOUT_INFO, APP_ABOUT_STARTUP_INFO


@pytest.mark.smoke
@pytest.mark.api
@allure.title("Проверка получения информации о приложении")
def test_about_app_info(unauthorized_client: ApiClient):
    """Проверка получения информации о приложении.

    GET /api/app/about
    """
    response = get_app_info(unauthorized_client)
    assert_status_code(response, HTTPStatus.OK)
    assert_schema(response, APP_ABOUT_INFO)


@pytest.mark.smoke
@pytest.mark.api
@allure.title("Получение информации о параметрах запуска приложения")
def test_about_app_startup_info(unauthorized_client: ApiClient):
    """Получение информации о параметрах запуска приложения.

    GET /api/app/about/startup-info
    """
    response = get_app_startup_info(unauthorized_client)
    assert_status_code(response, HTTPStatus.OK)
    assert_schema(response, APP_ABOUT_STARTUP_INFO)
