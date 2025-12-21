from requests import Response

from library.api.api_client import ApiClient
from library.echo import routes


def get_echo(
    client: ApiClient, headers: dict[str, str] | None = None, **params: dict | None
) -> Response:
    """Отправка echo-запроса методом GET.

    :param ApiClient client: API-клиент для отправки запросов
    :return Response: ответ сервера
    """
    return client.get(routes.ECHOER_REST, headers, **params)


def post_echo(
    client: ApiClient, headers: dict[str, str] | None = None, body=None
) -> Response:
    """Отправка echo-запроса методом POST.

    :param ApiClient client: API-клиент для отправки запросов
    :return Response: ответ сервера
    """
    return client.post(routes.ECHOER_REST, headers, body)


def put_echo(
    client: ApiClient, headers: dict[str, str] | None = None, body=None
) -> Response:
    """Отправка echo-запроса методом PUT.

    :param ApiClient client: API-клиент для отправки запросов
    :return Response: ответ сервера
    """
    return client.put(routes.ECHOER_REST, headers, body)


def patch_echo(
    client: ApiClient, headers: dict[str, str] | None = None, **params: dict | None
) -> Response:
    """Отправка echo-запроса методом GET.

    :param ApiClient client: API-клиент для отправки запросов
    :return Response: ответ сервера
    """
    return client.patch(routes.ECHOER_REST)


def detele_echo(
    client: ApiClient, headers: dict[str, str] | None = None, **params: dict | None
) -> Response:
    """Отправка echo-запроса методом GET.

    :param ApiClient client: API-клиент для отправки запросов
    :return Response: ответ сервера
    """
    return client.delete(routes.ECHOER_REST, headers, **params)
