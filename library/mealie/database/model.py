"""Модуль моделей таблиц для работа с БД Mealie."""

import sqlalchemy as db
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Базовый класс для объявления моделей таблиц БД Mealie."""


class ShoppingListItems(Base):
    """Класс представления таблицы 'shopping_list_items'."""

    __tablename__ = "shopping_list_items"

    quantity = db.Column()
    note = db.Column()
    shopping_list_id = db.Column(primary_key=True)
    food_id = db.Column()
    unit_id = db.Column()
    created_at = db.Column()
    label_id = db.Column()


class ShoppingLists(Base):
    """Класс представления таблицы 'shopping_lists'."""

    __tablename__ = "shopping_lists"

    id = db.Column(primary_key=True)
    user_id = db.Column()
    name = db.Column(db.VARCHAR)


class Users(Base):
    """Класс представления таблицы 'users'."""

    __tablename__ = "users"

    id = db.Column(primary_key=True)
    username = db.Column()


class IngredientFoods(Base):
    """Класс представления таблицы 'ingredient_foods'."""

    __tablename__ = "ingredient_foods"

    name = db.Column()
    plural_name = db.Column()
    id = db.Column(primary_key=True)


class IngredientUnits(Base):
    """Класс представления таблицы 'ingredient_units'."""

    __tablename__ = "ingredient_units"

    name = db.Column()
    plural_name = db.Column()
    id = db.Column(primary_key=True)
