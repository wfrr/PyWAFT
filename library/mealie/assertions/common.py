"""Общие проверки."""

import allure


@allure.step("Проверка соответствия строки ожидаемому значению")
def assert_strings_equal(value: str, exp_value: str, msg: str = ""):
    """Проверка соответствия строки ожидаемому значению.

    :param str value: значение для сравнения
    :param str exp_value: ожидаемое значение
    :param str msg: сообщение об ошибке, значение по умолчанию ""
    """
    assert value == exp_value, msg


@allure.step("Проверка соответствия числового значения ожидаемому")
def assert_ints_equal(value: int, exp_value: int, msg: str = ""):
    """Проверка соответствия числового значения ожидаемому.

    :param int value: значение для сравнения
    :param int exp_value: ожидаемое значение
    :param str msg: сообщение об ошибке, значение по умолчанию ""
    """
    assert value == exp_value, msg
