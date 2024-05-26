"""Модуль настроечных данных браузеров"""
from dataclasses import dataclass
from typing import Union


@dataclass
class BrowserData:
    """Класс настроечных данных браузера"""

    name: str
    version: str
    cli_args: list[str]
    prefs: list[dict[str, Union[bool, str, int, dict, list[str]]]]
