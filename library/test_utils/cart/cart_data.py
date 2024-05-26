"""Модуль данных стенда Cart"""
from dataclasses import dataclass
from typing import Union

from library.test_utils.stand_data import StandData


@dataclass
class CartData(StandData):
    """Класс данных стенда Cart"""

    app: dict[str, str]
    db: dict[str, str]
    users: dict[str, dict[str, Union[str, int]]]
