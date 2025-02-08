import json
import random
from http import HTTPStatus
from string import ascii_letters

import allure
import pytest

from library.api_client import ApiClient
from library.core.app_data import AppData
from library.mealie.api.actions.admin_crud import (
    create_user,
    delete_user,
    get_all_users,
)
from library.mealie.api.actions.user_crud import update_user
from library.mealie.api.models import ALL_USERS, CREATE_USER
from library.mealie.assertions.api import assert_schema, assert_status_code


@pytest.mark.api
@allure.title("Тест получения списка пользователей")
def test_list_users(admin_authorized_client: ApiClient):
    """Тест получения списка пользователей.

    GET /api/admin/users
    """
    users_resp = get_all_users(
        admin_authorized_client, params={"orderBy": "id", "orderDirection": "desc"}
    )
    assert_status_code(users_resp, HTTPStatus.OK)
    assert_schema(users_resp, ALL_USERS)


@pytest.mark.api
@allure.title("Тест получения списка пользователей")
def test_create_user(admin_authorized_client: ApiClient):
    """Тест получения списка пользователей.

    POST /api/admin/users
    """
    username = "test_" + "".join(random.choice(ascii_letters) for _ in range(10))
    password = "".join(random.choice(ascii_letters) for _ in range(15))
    body = json.dumps(
        {
            "email": f"{username}@test.com",
            "fullName": "Test",
            "username": username,
            "password": password,
        }
    )
    create_user_resp = create_user(admin_authorized_client, body=body)
    assert_status_code(create_user_resp, HTTPStatus.CREATED)
    assert_schema(create_user_resp, CREATE_USER)


@pytest.mark.api
@allure.title("Тест изменения пароля пользователя")
def test_update_user(user_authorized_client: ApiClient, stand: AppData):
    """Тест изменения пароля пользователя.

    PUT /api/users/password
    """
    headers = {"Content-Type": "application/json"}
    body = json.dumps(
        {"currentPassword": stand.users["regular"]["password"], "newPassword": "12345678"}
    )
    updated_user_resp = update_user(user_authorized_client, headers=headers, body=body)
    assert_status_code(updated_user_resp, HTTPStatus.OK)


@pytest.mark.api
@allure.title("Тест удаления пользовател")
def test_delete_user(admin_authorized_client: ApiClient, test_user_data: list):
    """Тест удаления пользователя.

    DELETE /api/admin/users/{id}
    """
    delete_user_resp = delete_user(admin_authorized_client, test_user_data[0])
    assert_status_code(delete_user_resp, HTTPStatus.OK)
