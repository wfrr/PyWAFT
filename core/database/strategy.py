"""Модуль стратегии для подключения к БД."""

from abc import ABC, abstractmethod
from collections.abc import Sequence

from sqlalchemy import Select, create_engine, text
from sqlalchemy.orm import Session


class DataBaseStrategy(ABC):
    """Абстрактный базовый класс стратегии для БД."""

    @abstractmethod
    def execute_query(self, q: str, conf: dict[str, str]) -> str:
        """Абстрактный метод выполнения sql-запроса.

        :param str q: SQL-запрос к БД
        :param dict[str, str] conf: данные для подключения к БД
        """


class PostrgreSQLDataBaseStrategy(DataBaseStrategy):
    """Cтратегия для работы с БД PostrgreSQL."""

    def __init__(self, conf: dict[str, str]) -> None:
        """Инициализация стратегии."""
        engine = create_engine(
            f'postgresql+psycopg2://{conf["username"]}:{conf["password"]}@{conf["host"]}:{conf["port"]}/{conf["name"]}',
            echo=False,
            pool_size=5,
            max_overflow=10,
        )
        self._session = Session(bind=engine)

    def execute_query(self, q: Select) -> Sequence:
        """Метод выполнения sql-запроса.

        :params str q: SQL-запрос для выполнения
        """
        return self._session.execute(q).all()

    def execute_query_text(self, text_query: str) -> Sequence:
        """Метод выполнения sql-запроса из строки текста.

        :params str text_query: SQL-запрос для выполнения в виде текста
        """
        query = text(text_query)
        return self._session.execute(query).all()
