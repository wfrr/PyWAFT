"""Проверки, связанные с API."""

from jsonschema import validate
from requests import Response


def assert_status_code(response: Response, expected_code: int) -> None:
    """Сравнение кода ответа с ожидаемым.

    :param response: ответ от сервера
    :param expected_code: ожидаемый код ответа
    :raises AssertionError: значения не совпали
    """
    assert response.status_code == expected_code


def assert_schema(response: Response, schema) -> None:
    """Проверка тела ответа на соответствие схеме.

    :param response: ответ от сервера
    :param schema: модель для проверки схемы json
    :raises ValidationError: тело ответа не соответствует схеме.
    """
    validate(instance=response.json(), schema=schema)
