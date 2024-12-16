"""Модуль клиента для исполнения запросов к БД."""

from collections.abc import Sequence

from sqlalchemy import Select

from core.database.context import DataBaseContext
from core.database.strategy import PostrgreSQLDataBaseStrategy


class PostgreSQLDBClient:
    """Клиент для выполнения SQL-запросов к БД Postrges."""

    def __init__(self, conf: dict[str, str]) -> None:
        """Инициализация клиента Postrges."""
        self._context = DataBaseContext(PostrgreSQLDataBaseStrategy(conf))

    def execute_query(self, query: str) -> Sequence:
        """Выполнение SQL-запросов к БД через ORM."""
        return self._context.execute_query(query)

    def execute_query_text(self, query: Select) -> Sequence:
        """Выполнение SQL-запросов к БД в виде строки."""
        return self._context.execute_query_text(query)
