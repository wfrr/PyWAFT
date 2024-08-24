"""Модуль данных тестируемой системы"""
from dataclasses import dataclass


@dataclass
class AppData:
    """Класс данных тестируемой системы"""

    app: dict[str, str]
    db: dict[str, str]
    users: dict[str, dict[str, str]]
