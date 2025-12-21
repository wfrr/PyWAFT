"""Модуль с бизнесовыми методами по работе с CRUD-операциями администратора."""

from uuid import UUID

import allure
from requests import Response

from library.api.api_client import ApiClient
from library.mealie.api import routes


@allure.step("Получение всех пользователей")
def get_all_users(
    client: ApiClient, headers: dict[str, str] | None = None, **params: dict | None
) -> Response:
    """Получение всех пользователей.

    :param ApiClient client: API-клиент для отправки запросов
    :params dict[str, str] headers: заголовки для передачи в запросе
    :params dict params: параметры представления данных пользователей в ответе
    :return Response: ответ сервера
    """
    return client.get(routes.ADMIN_ALL_USERS, headers=headers, params=params)


@allure.step("Создание пользователя")
def create_user(
    client: ApiClient, headers: dict[str, str] | None = None, body=None
) -> Response:
    """Создание пользователя.

    :param ApiClient client: API-клиент для отправки запросов
    :params dict[str, str] headers: заголовки для передачи в запросе
    :params dict body: параметры пользователя
    :return Response: ответ сервера
    """
    return client.post(routes.ADMIN_CREATE_USER, headers=headers, body=body)


@allure.step("Удаление пользователя")
def delete_user(
    client: ApiClient, user_id: UUID | str, headers: dict[str, str] | None = None
) -> Response:
    """Удаление пользователя.

    :param ApiClient client: API-клиент для отправки запросов
    :params dict[str, str] headers: заголовки для передачи в запросе
    :return Response: ответ сервера
    """
    return client.delete(routes.ADMIN_DELETE_USER.format(user_id), headers=headers)
