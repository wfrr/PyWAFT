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


def select_shopping_list_by_name(
    conf: dict[str, str], shopping_list_name: str, username: str
) -> list[list[str]]:
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
    return [
        [row.item, row.quantity, row.units, row.note]
        for row in PostgreSQLDBClient(conf).execute_query_text(statement)
    ]


def select_shopping_list_by_name_orm(
    conf: dict[str, str], shopping_list_name: str, username: str
) -> list[list[str]]:
    """Получение данных пользователя по Id.

    :param dict conf: данные для подключения к БД
    :param str shopping_list_name: название списка покупок
    :param str username: имя пользователя
    :returns list: список с данными
    """
    statement = (
        select(
            IngredientFoods.name.label("item"),
            ShoppingListItems.quantity,
            IngredientUnits.name.label("units"),
            ShoppingListItems.note,
        )
        .select_from(ShoppingListItems)
        .join(ShoppingLists, ShoppingListItems.shopping_list_id == ShoppingLists.id)
        .join(Users, ShoppingLists.user_id == Users.id)
        .join(
            IngredientFoods, ShoppingListItems.food_id == IngredientFoods.id, isouter=True
        )
        .join(
            IngredientUnits,
            ShoppingListItems.unit_id == IngredientUnits.id,
            isouter=True,
        )
        .where(Users.username == username)
        .where(ShoppingLists.name == shopping_list_name)
        .order_by(ShoppingListItems.created_at.desc())
    )
    return [
        [row.item, row.quantity, row.units, row.note]
        for row in PostgreSQLDBClient(conf).execute_query(statement)
    ]


def select_test_users_id_by_name(conf: dict[str, str]) -> list[list[str]]:
    """Получение id тестовых пользователей.

    :param dict conf: данные для подключения к БД
    :returns list: список с данными
    """
    statement = """
       SELECT
           U.ID,
           G.NAME AS GROUP,
           H.NAME AS HOUSEHOLD,
           U.GROUP_ID,
           U.HOUSEHOLD_ID,
           U.CACHE_KEY,
           G.SLUG AS GROUP_SLUG,
           H.SLUG AS HOUSEHOLD_SLUG
       FROM
           PUBLIC.USERS U
           JOIN PUBLIC.GROUPS G ON U.GROUP_ID = G.ID
           JOIN PUBLIC.HOUSEHOLDS H ON U.HOUSEHOLD_ID = H.ID
       WHERE
           U.USERNAME LIKE 'test_%';
    """
    return [
        [
            row.id,
            row.group,
            row.household,
            row.group_id,
            row.household_id,
            row.cache_key,
            row.group_slug,
            row.household_slug,
        ]
        for row in PostgreSQLDBClient(conf).execute_query_text(statement)
    ]
