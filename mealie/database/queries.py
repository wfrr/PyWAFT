"""Модуль методов запросов к БД Mealie."""

from core.database.context import DataBaseContext
from core.database.strategy import PostrgreSQLDataBaseStrategy


def select_shopping_list_by_name(conf: dict[str, str], shopping_list_name: str, username: str) -> list[list[str]]:
    """Получение данных пользователя по Id.

    :param dict conf: данные для подключения к БД
    :param str shopping_list_name: название списка покупок
    :param str username: имя пользователя
    :returns list: список с данными
    """
    context = DataBaseContext(PostrgreSQLDataBaseStrategy(conf))
    statement = f"""
       SELECT
        SL.NAME AS SHOPPING_LIST,
        INF.NAME AS ITEM,
        SLI.QUANTITY,
        IU.NAME AS UNITS,
        SLI.NOTE
       FROM
           PUBLIC.SHOPPING_LIST_ITEMS SLI
           JOIN PUBLIC.SHOPPING_LISTS SL ON SLI.SHOPPING_LIST_ID = SL.ID
           JOIN PUBLIC.USERS U ON U.ID = SL.USER_ID
           LEFT JOIN PUBLIC.INGREDIENT_FOODS INF ON SLI.FOOD_ID = INF.ID
           LEFT JOIN PUBLIC.INGREDIENT_UNITS IU ON SLI.UNIT_ID = IU.ID
       WHERE
           U.USERNAME = '{username}'
           AND SL.NAME = '{shopping_list_name}'
       ORDER BY SLI.CREATED_AT DESC;
    """
    return [[row.item, row.quantity, row.units, row.note] for row in context.execute_query_text(statement)]
