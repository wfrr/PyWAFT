"""Модуль с бизнесовыми методами по получению данных о приложении."""

from requests import Response

from library.api_client import ApiClient
from library.mealie.api import routes


def get_app_info(client: ApiClient) -> Response:
    """Получение информации о приложении.

    :param ApiClient client: API-клиент для отправки запросов
    :return Response: ответ сервера
    """
    return client.get(routes.APP_ABOUT_INFO)


def get_app_startup_info(client: ApiClient) -> Response:
    """Получение информации о параметрах запуска приложения.

    :param ApiClient client: API-клиент для отправки запросов
    :return Response: ответ сервера
    """
    return client.get(routes.APP_ABOUT_STARTUP_INFO)
