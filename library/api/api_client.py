"""Модуль API-клиента для выполнения HTTP-запросов."""

from typing import Any, MutableMapping, Sequence
from urllib.parse import urljoin

from requests import Response, Session


class ApiClient:
    """Клиент API для выполнения запросов."""

    def __init__(self, base_url: str) -> None:
        self._base_url = base_url
        self._session = Session()
        self._timout = 120
        self._session.headers = {"User-Agent": "pywaft"}

    @property
    def headers(self) -> MutableMapping[str, str | bytes]:
        return self._session.headers

    # TODO: setter -> __add__
    @headers.setter
    def headers(self, headers: MutableMapping[str, str | bytes]) -> None:
        self._session.headers = headers

    def add_headers(self, headers: MutableMapping[str, str | bytes]) -> None:
        self._session.headers.update(headers)

    def delete_headers(self, headers: str | Sequence[str]) -> None:
        if isinstance(headers, str):
            del self._session.headers[headers]
        elif isinstance(headers, Sequence):
            for header in headers:
                del self._session.headers[header]

    def get(
        self, route: str, headers: dict | None = None, **params: dict | None
    ) -> Response:
        if headers:
            self.add_headers(headers)
        url = urljoin(self._base_url, route)
        return self._session.get(url, params=params)

    def post(
        self,
        route: str,
        headers: dict | None = None,
        body: Any | None = None,
        json: Any | None = None,
    ) -> Response:
        if headers:
            self.add_headers(headers)
        url = urljoin(self._base_url, route)
        return self._session.post(url, data=body, json=json)

    def put(self, route: str, headers: dict | None = None, body=None) -> Response:
        if headers:
            self.add_headers(headers)
        url = urljoin(self._base_url, route)
        return self._session.put(url, data=body)

    def patch(self, route: str, headers: dict | None = None, body=None) -> Response:
        if headers:
            self.add_headers(headers)
        url = urljoin(self._base_url, route)
        return self._session.patch(url, data=body)

    def delete(
        self, route: str, headers: dict | None = None, **params: dict | None
    ) -> Response:
        if headers:
            self.add_headers(headers)
        url = urljoin(self._base_url, route)
        return self._session.delete(url, params=params)
