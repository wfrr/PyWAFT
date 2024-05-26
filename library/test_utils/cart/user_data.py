"""Модуль работы с данными клиентов"""

from dataclasses import dataclass
from typing import Optional

from library.test_utils.cart.utils import random_string


@dataclass
class PersonInfo:
    """Класс персональных данных"""

    first_name: str
    last_name: str

    def __init__(self, first_name: Optional[str] = None, last_name: Optional[str] = None):
        self.first_name = first_name or random_string(5)
        self.last_name = last_name or random_string(8)
