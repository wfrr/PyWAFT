import allure


def assert_strings_equal(value1: str, value2: str, msg: str = '') -> None:
    """
    Проверка равенства значений

    :param str msg: сообщение об ошибке
    :param str value1: первое значение для проверки соответствия
    :param str value2: второе значение для проверки соответствия
    """
    with allure.step(f'Проверка равенства значений {value1} и {value2}'):
        assert value1 == value2, msg
