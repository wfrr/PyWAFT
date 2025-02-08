from http import HTTPStatus

import pytest

from library.api_client import ApiClient
from library.mealie.api.actions.about_app_info import get_app_info, get_app_startup_info
from library.mealie.api.models import APP_ABOUT_INFO, APP_ABOUT_STARTUP_INFO
from library.mealie.assertions.api import assert_schema, assert_status_code


@pytest.mark.smoke
@pytest.mark.api
def test_about_app_info(unauthorized_client: ApiClient):
    """
    GET /api/app/about
    """
    response = get_app_info(unauthorized_client)
    assert_status_code(response, HTTPStatus.OK)
    assert_schema(response, APP_ABOUT_INFO)


@pytest.mark.smoke
@pytest.mark.api
def test_about_app_startup_info(unauthorized_client: ApiClient):
    """
    GET /api/app/about/startup-info
    """
    response = get_app_startup_info(unauthorized_client)
    assert_status_code(response, HTTPStatus.OK)
    assert_schema(response, APP_ABOUT_STARTUP_INFO)
