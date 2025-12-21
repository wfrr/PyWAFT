import allure
import pytest

from library.api.api_client import ApiClient
from library.assertions.common import assert_strings_equal
from library.echo.api.rpc import call_echo


@pytest.mark.api
@allure.title("Тест вызова метода echo через RPC")
def test_rpc(api_client: ApiClient):
    """Тест вызова метода echo через RPC."""
    msg = "Hi rpc"
    resp = call_echo(api_client, msg)
    assert_strings_equal(resp["result"]["op_result"]["params"][0], msg)
