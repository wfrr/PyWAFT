"""Модуль методов запросов к БД Mealie."""

from sqlalchemy import select

from library.db_client import PostgreSQLDBClient

from .model import (
    IngredientFoods,
    IngredientUnits,
    ShoppingListItems,
    ShoppingLists,
    Users,
)


def select_shopping_list_by_name(conf: dict[str, str], shopping_list_name: str, username: str) -> list[list[str]]:
    """Получение данных пользователя по Id.

    :param dict conf: данные для подключения к БД
    :param str shopping_list_name: название списка покупок
    :param str username: имя пользователя
    :returns list: список с данными
    """
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
    return [[row.item, row.quantity, row.units, row.note] for row
                in PostgreSQLDBClient(conf).execute_query_text(statement)]


def select_shopping_list_by_name_orm(conf: dict[str, str], shopping_list_name: str, username: str) -> list[list[str]]:
    """Получение данных пользователя по Id.

    :param dict conf: данные для подключения к БД
    :param str shopping_list_name: название списка покупок
    :param str username: имя пользователя
    :returns list: список с данными
    """
    statement = (
        select(
            IngredientFoods.name.label('item'),
            ShoppingListItems.quantity,
            IngredientUnits.name.label('units'),
            ShoppingListItems.note,
        )
        .select_from(ShoppingListItems)
        .join(ShoppingLists, ShoppingListItems.shopping_list_id == ShoppingLists.id)
        .join(Users, ShoppingLists.user_id == Users.id)
        .join(IngredientFoods, ShoppingListItems.food_id == IngredientFoods.id, isouter=True)
        .join(
            IngredientUnits,
            ShoppingListItems.unit_id == IngredientUnits.id,
            isouter=True,
        )
        .where(Users.username == username)
        .where(ShoppingLists.name == shopping_list_name)
        .order_by(ShoppingListItems.created_at.desc())
    )
    return [[row.item, row.quantity, row.units, row.note] for row in PostgreSQLDBClient(conf).execute_query(statement)]
