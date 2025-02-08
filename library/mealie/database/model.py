"""Модуль моделей таблиц для работа с БД Mealie."""

import sqlalchemy as db
from sqlalchemy.orm import DeclarativeBase, Mapped


class Base(DeclarativeBase):
    """Базовый класс для объявления моделей таблиц БД Mealie."""


class ShoppingListItems(Base):
    """Класс представления таблицы 'shopping_list_items'."""

    __tablename__ = "shopping_list_items"

    quantity: Mapped[float] = db.Column()
    note: Mapped[str] = db.Column()
    shopping_list_id: Mapped[str] = db.Column(primary_key=True)
    food_id: Mapped[str] = db.Column()
    unit_id: Mapped[str] = db.Column()
    created_at: Mapped[str] = db.Column()


class ShoppingLists(Base):
    """Класс представления таблицы 'shopping_lists'."""

    __tablename__ = "shopping_lists"

    id: Mapped[str] = db.Column(primary_key=True)
    user_id: Mapped[str] = db.Column()
    name: Mapped[str] = db.Column(db.VARCHAR)


class Users(Base):
    """Класс представления таблицы 'users'."""

    __tablename__ = "users"

    id: Mapped[str] = db.Column(primary_key=True)
    username: Mapped[str] = db.Column()


class IngredientFoods(Base):
    """Класс представления таблицы 'ingredient_foods'."""

    __tablename__ = "ingredient_foods"

    name: Mapped[str] = db.Column()
    id: Mapped[str] = db.Column(primary_key=True)


class IngredientUnits(Base):
    """Класс представления таблицы 'ingredient_units'."""

    __tablename__ = "ingredient_units"

    name: Mapped[str] = db.Column()
    id: Mapped[str] = db.Column(primary_key=True)
