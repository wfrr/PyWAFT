"""Модуль работы с данными клиентов"""

import dataclasses
from typing import Optional

from library.utils import random_string


@dataclasses.dataclass
class PersonInfo():
    """Класс персональных данных"""

    def __init__(self, first_name: Optional[str] = None, last_name: Optional[str] = None):
        self.first_name = first_name or random_string(5)
        self.last_name = last_name or random_string(8)
