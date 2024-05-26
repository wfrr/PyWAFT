"""Модуль настроечных данных браузеров"""
from dataclasses import dataclass


@dataclass
class BrowserData:
    """Класс настроечных данных браузера"""

    name: str
    version: str
    cli_args: list[str]
