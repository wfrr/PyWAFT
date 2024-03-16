"""Модуль инициализации соединения с БД OpenCart"""

from typing import Mapping

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def init_db_connection(conf: Mapping[str, str]) -> Session:
    """Инициализация подключения к БД

    :param Mapping[str, str] conf: данные для подключения
    :returns Session: подключение к бд
    """
    engine_ = create_engine(
        f'mysql+pymysql://{conf["username"]}:{conf["password"]
                                              }@{conf["host"]}:{conf["port"]}/{conf["db_name"]}',
        echo=False, pool_size=5, max_overflow=10
    )
    return Session(bind=engine_)
