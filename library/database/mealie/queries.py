"""Модуль методов запросов к БД Mealie."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from ._models import (
    IngredientFoods,
    IngredientUnits,
    ShoppingListItems,
    ShoppingLists,
    Users,
)


def select_shopping_list_by_name(session: Session, shopping_list_name: str, username: str) -> list[list[str]]:
    """Получение данных покупателя по Id.

    Выполнения SQL-запроса:
    ```SELECT
        SL.NAME AS SHOPPING_LIST,
        INF.NAME AS ITEM,
        SLI.QUANTITY,
        IU.NAME AS UNITS,
        SLI.NOTE
       FROM
           PUBLIC.SHOPPING_LIST_ITEMS SLI
           JOIN PUBLIC.SHOPPING_LISTS SL ON SLI.SHOPPING_LIST_ID = SL.ID
           JOIN PUBLIC.USERS U ON U.ID = SL.USER_ID
           JOIN PUBLIC.INGREDIENT_FOODS INF ON SLI.FOOD_ID = INF.ID
           LEFT JOIN PUBLIC.INGREDIENT_UNITS IU ON SLI.UNIT_ID = IU.ID
       WHERE
           U.USERNAME = '{username}'
           AND SL.NAME = '{name}'
           ```

    :param Session session: сессия БД
    :param str shopping_list_name: название списка покупок
    :param str username: имя пользователя
    :returns list: список с данными
    """
    with session as s:
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
            .join(IngredientFoods, ShoppingListItems.food_id == IngredientFoods.id)
            .join(
                IngredientUnits,
                ShoppingListItems.unit_id == IngredientUnits.id,
                isouter=True,
            )
            .where(Users.username == username)
            .where(ShoppingLists.name == shopping_list_name)
        )

        results = s.execute(statement).all()

    return [[row.item, row.quantity, row.units] for row in results]
