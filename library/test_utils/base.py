"""Базовые вспомогательные места для тестов"""

from typing import Optional

import allure


def assert_strings_equal(value1: str, value2: str, msg: Optional[str] = None) -> None:
    """
    Проверка равенства значений

    :param str msg: сообщение об ошибке
    :param str value1: первое значение для проверки соответствия
    :param Optional[str] value2: второе значение для проверки соответствия
    """
    with allure.step(f'Проверка равенства значений {value1} и {value2}'):
        assert value1 == value2, msg
