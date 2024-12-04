"""Модуль контекста для подключения к БД."""

from collections.abc import Sequence

from sqlalchemy import Select

from .strategy import DataBaseStrategy


class DataBaseContext:
    """Класс контекста БД для выполнения SQL-запроса."""

    def __init__(self, strategy: DataBaseStrategy | None = None) -> None:
        """Инициализация контекста.

        :params DataBaseStrategy strategy: выбранная стратегия
        """
        self._strategy = strategy

    def set_strategy(self, strategy: DataBaseStrategy) -> None:
        """Установка новой стратегии.

        :params DataBaseStrategy strategy: выбранная стратегия
        """
        self._strategy = strategy

    def execute_query(self, q: Select) -> Sequence:
        """Выполнение SQL-запроса через ORM с  использованием выбранной стратегии.

        :params str q: SQL-запрос для выполнения
        """
        return self._strategy.execute_query(q)

    def execute_query_text(self, q: str) -> Sequence:
        """Выполнение SQL-запроса в виде строки с  использованием выбранной стратегии.

        :params str q: SQL-запрос для выполнения
        """
        return self._strategy.execute_query_text(q)
