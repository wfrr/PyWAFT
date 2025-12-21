from requests import Response

from library.api.api_client import ApiClient
from library.api.soap_client import SoapClient
from library.echo import routes


def call_echo(client: SoapClient, msg: str) -> str:
    """Отправка вызова метода echo через SOAP.

    :param SoapClient client: SOAP-клиент для отправки запросов
    :return str: ответ сервера
    """
    return client.Echo(msg)


def call_wsdl(client: ApiClient) -> Response:
    """Отправка вызова получения WSDL.

    :param SoapClient client: SOAP-клиент для отправки запросов
    :return str: ответ сервера
    """
    return client.get(routes.ECHOER_SOAP_WSDL)
