"""Модуль настроечных данных браузеров"""
from dataclasses import dataclass
from typing import Union


@dataclass
class BrowserData:
    """Класс настроечных данных браузера"""

    name: str
    version: str
    cli_args: list[str]
    prefs: list[dict[str, Union[bool, str, int]]]
    page_load_strategy: str
    accept_insecure_certs: bool
    unhandled_prompt_behavior: str
