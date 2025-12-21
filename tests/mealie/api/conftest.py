import json
import random
from http import HTTPStatus
from string import ascii_letters

import pytest

from library.api.api_client import ApiClient
from library.assertions.api import assert_status_code
from library.core.app_data import AppData
from library.mealie.api.actions.admin_crud import create_user
from library.mealie.api.actions.user_auth import auth_user
from library.mealie.database.queries import select_test_users_id_by_name


@pytest.fixture
def admin_authorized_client(stand: AppData) -> ApiClient:
    """Авторизованный под пользователем администратора API-клиент теста."""
    username = stand.users["admin"]["username"]
    password = stand.users["admin"]["password"]
    remember_me = "false"
    client = ApiClient(base_url=stand.app["url"])
    auth_resp = auth_user(
        client,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body=f"username={username}&password={password}&remember_me={remember_me}",
    )
    assert_status_code(auth_resp, HTTPStatus.OK)
    if "Content-Type" in client.headers.keys():
        client.delete_headers("Content-Type")
    client.add_headers({"Authorization": f"Bearer {auth_resp.json()['access_token']}"})
    return client


@pytest.fixture
def user_authorized_client(stand: AppData) -> ApiClient:
    """Авторизованный под обычным пользователем API-клиент теста."""
    username = stand.users["regular"]["username"]
    password = stand.users["regular"]["password"]
    remember_me = "false"
    client = ApiClient(base_url=stand.app["url"])
    auth_resp = auth_user(
        client,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body=f"username={username}&password={password}&remember_me={remember_me}",
    )
    assert_status_code(auth_resp, HTTPStatus.OK)
    if "Content-Type" in client.headers.keys():
        client.delete_headers("Content-Type")
    client.add_headers({"Authorization": f"Bearer {auth_resp.json()['access_token']}"})
    return client


@pytest.fixture
def unauthorized_client(stand: AppData) -> ApiClient:
    """API-клиент теста."""
    return ApiClient(base_url=stand.app["url"])


@pytest.fixture
def test_user_data(admin_authorized_client: ApiClient, stand: AppData) -> list:
    test_users = select_test_users_id_by_name(stand.db)
    if not test_users:
        username = "test_" + "".join(random.choice(ascii_letters) for _ in range(10))
        body = json.dumps({
            "email": f"{username}@test.com",
            "fullName": "Test",
            "username": username,
            "password": "1234567890",
        })
        resp = create_user(admin_authorized_client, body=body)
        assert_status_code(resp, HTTPStatus.CREATED)
        return [resp.json()["id"]]
    return test_users[0]
