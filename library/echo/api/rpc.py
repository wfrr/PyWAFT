from library.api.api_client import ApiClient
from library.echo import routes


def call_echo(client: ApiClient, params: str | dict | list) -> dict:
    """Отправка вызов метода echo через RPC.

    :param ApiClient client: API-клиент для отправки запросов
    :return Response: ответ сервера
    """
    payload = {
        "method": "echo",
        "params": [params],
        "jsonrpc": "2.0",
        "id": 1,
    }
    return client.post(routes.ECHOER_RPC, json=payload).json()
