"""Модуль моделей таблиц для работа с БД Mealie."""

from sqlalchemy.ext.declarative import DeferredReflection
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Базовый класс для объявления моделей таблиц БД Mealie."""


class Reflected(DeferredReflection):
    """Базовый класс для отображения существующих таблиц из БД.

    Позволяет определить необходимые таблицы до инициализации соединения:
        https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#using-deferredreflection
    """
    __abstract__ = True


class ShoppingListItems(Reflected, Base):
    """Класс представления таблицы 'shopping_list_items'."""

    __tablename__ = 'shopping_list_items'

    quantity: Mapped[float]
    note: Mapped[str]
    shopping_list_id: Mapped[str]
    food_id: Mapped[str]
    unit_id: Mapped[str]


class ShoppingLists(Reflected, Base):
    """Класс представления таблицы 'shopping_lists'."""

    __tablename__ = 'shopping_lists'

    id: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[str]
    name: Mapped[str]


class Users(Reflected, Base):
    """Класс представления таблицы 'users'."""

    __tablename__ = 'users'

    id: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str]


class IngredientFoods(Reflected, Base):
    """Класс представления таблицы 'ingredient_foods'."""

    __tablename__ = 'ingredient_foods'

    name: Mapped[str]
    id: Mapped[str] = mapped_column(primary_key=True)


class IngredientUnits(Reflected, Base):
    """Класс представления таблицы 'ingredient_units'."""

    __tablename__ = 'ingredient_units'

    name: Mapped[str]
    id: Mapped[str] = mapped_column(primary_key=True)
