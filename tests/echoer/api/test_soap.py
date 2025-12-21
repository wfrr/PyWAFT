import json
from http import HTTPStatus

import allure
import pytest

from library.api.api_client import ApiClient
from library.api.soap_client import SoapClient
from library.assertions.api import assert_schema_str, assert_status_code
from library.assertions.common import aseert_string_contains, assert_strings_equal
from library.echo.api.soap import call_echo, call_wsdl
from library.echo.models import ECHOER_SCHEMA


@pytest.mark.api
@allure.title("Тест вызова метода echo через SOAP")
def test_soap(soap_client: SoapClient):
    msg = "Hi soap"
    resp = call_echo(soap_client, msg)
    assert_schema_str(resp, ECHOER_SCHEMA)
    assert_strings_equal(str(json.loads(resp)["op_result"]), msg)


@pytest.mark.api
@allure.title("Тест получения WSDL")
def test_wsdl(api_client: ApiClient):
    resp = call_wsdl(api_client)
    assert_status_code(resp, HTTPStatus.OK)
    aseert_string_contains(resp.text, 'name="EchoRequest"')
