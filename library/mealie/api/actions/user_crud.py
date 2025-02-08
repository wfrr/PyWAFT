"""Модуль с бизнесовыми методами по работе с CRUD-операциями пользователя."""

from requests import Response

from library.api_client import ApiClient
from library.mealie.api import routes


def update_user(
    client: ApiClient,
    headers: dict[str, str] | None = None,
    body: str | None = None,
) -> Response:
    """Изменение пользователя.

    :param ApiClient client: API-клиент для отправки запросов
    :params dict[str, str] headers: заголовки для передачи в запросе
    :params dict params: параметры пользователя
    :return Response: ответ сервера
    """
    return client.put(routes.UPDATE_USER_PASSWORD, headers=headers, body=body)
