"""Модуль работы с БД OpenCart"""

from .queries import select_customer_by_id, select_customers_order_by_firstname
from .connection import init_db_connection
