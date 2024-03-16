"""Модуль методов запросов к БД OpenCart"""

from typing import Mapping, Union

from sqlalchemy import select
from sqlalchemy.orm import Session

from library.database.cart.models import Cart, Customer, Product, ProductDescription


def select_customer_by_id(session: Session, customer_id: int) -> Mapping[str, Union[str, int]]:
    """
    Получение данных покупателя по Id

    Выполнения SQL-запроса: SELECT c.firstname, c.lastname, c.email FROM store.oc_customer c
        WHERE c.customer_id = customer_id

    :param Session session: сессия БД
    :param int customer_id: Id покупателя
    :returns Mapping: словарь с данными покупателя
    """
    with session as s:
        statement = select(
            Customer.firstname, Customer.lastname, Customer.email
        ).where(
            Customer.customer_id == customer_id
        )
        row = s.execute(statement).first()
    return {
        Customer.firstname.name: row.firstname,
        Customer.lastname.name: row.lastname,
        Customer.email.name: row.email
    }


def select_customers_order_by_firstname(session: Session) -> list[Mapping[str, Union[str, int]]]:
    """
    Получение содержимого корзины покупателя

    Выполнения SQL-запроса: SELECT c.quantity, p.model, pd.name FROM store.oc_cart c, store.oc_product p,
        store.oc_product_description pd WHERE c.product_id = p.product_id AND c.product_id = pd.product_id
        ORDER BY c.cart_id ASC;


    :param Session session: сессия БД
    :return list: список данными по корзине покупателя
    """
    result = []
    with session as s:
        statement = select(Cart.quantity, Product.model, ProductDescription.name).select_from(Cart).where(
            Cart.product_id == Product.product_id,
            Cart.product_id == ProductDescription.product_id
        ).order_by(Cart.cart_id.asc())
        rows = s.execute(statement).all()
        for row in rows:
            result.append(
                {
                    Cart.quantity.name: row.quantity,
                    Product.model.name: row.model,
                    ProductDescription.name.name: row.name,
                }
            )
    return result
