"""Модуль с бизнесовыми методами по получению аутентификации пользователя."""

from requests import Response

from library.api_client import ApiClient
from library.mealie.api import routes


def auth_user(client: ApiClient, headers: dict, body: str) -> Response:
    """Аутентификация пользователя.

    :param ApiClient client: API-клиент для отправки запросов
    :param dict headers: заголовки запроса
    :param str body: тело запроса
    :return Response: ответ сервера
    """
    return client.post(routes.USER_AUTH, headers=headers, body=body)
