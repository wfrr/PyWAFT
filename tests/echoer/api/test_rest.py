from http import HTTPStatus

import allure
import pytest

from library.api.api_client import ApiClient
from library.assertions.api import assert_schema, assert_status_code
from library.echo.api.rest import detele_echo, get_echo, patch_echo, post_echo, put_echo
from library.echo.models import ECHOER_SCHEMA


@pytest.mark.api
@allure.title("Тест метода GET")
def test_get(api_client: ApiClient):
    """Тест метода GET.

    GET /echoer/rest
    """
    resp = get_echo(api_client, params={"filter": "id", "status": "completed"})
    assert_status_code(resp, HTTPStatus.OK)
    assert_schema(resp, ECHOER_SCHEMA)


@pytest.mark.api
@allure.title("Тест метода POST")
def test_post(api_client: ApiClient):
    """Тест метода POST.

    POST /echoer/rest
    """
    resp = post_echo(api_client, body="Hi ther!")
    assert_status_code(resp, HTTPStatus.OK)
    assert_schema(resp, ECHOER_SCHEMA)


@pytest.mark.api
@allure.title("Тест метода PUT")
def test_put(api_client: ApiClient):
    """Тест метода PUT.

    PUT /echoer/rest
    """
    resp = put_echo(api_client, body={"name": "Jack", "status": "employed"})
    assert_status_code(resp, HTTPStatus.OK)
    assert_schema(resp, ECHOER_SCHEMA)


@pytest.mark.api
@allure.title("Тест метода PATCH")
def test_patch(api_client: ApiClient):
    """Тест метода PATCH.

    PATCH /echoer/rest
    """
    resp = patch_echo(api_client, params={"is_locked": "true"})
    assert_status_code(resp, HTTPStatus.OK)
    assert_schema(resp, ECHOER_SCHEMA)


@pytest.mark.api
@allure.title("Тест метода DELETE")
def test_delete(api_client: ApiClient):
    """Тест метода DELETE.

    DELETE /echoer/rest
    """
    resp = detele_echo(api_client, params={"id": "2"})
    assert_status_code(resp, HTTPStatus.OK)
    assert_schema(resp, ECHOER_SCHEMA)
