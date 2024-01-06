from datetime import datetime
from decimal import Decimal

from sqlalchemy import Integer, String, Text, Boolean, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = 'oc_customer'

    customer_id: Mapped[int] = mapped_column('customer_id', Integer, nullable=False,
                                             autoincrement=True, primary_key=True, unique=True)
    customer_group_id: Mapped[int] = mapped_column('customer_group_id', Integer, nullable=False)
    store_id: Mapped[int] = mapped_column('store_id', Integer, default=0, nullable=False)
    language_id: Mapped[int] = mapped_column('language_id', Integer, nullable=False)
    firstname: Mapped[str] = mapped_column('firstname', String(32), nullable=False)
    lastname: Mapped[str] = mapped_column('lastname', String(32), nullable=False)
    email: Mapped[str] = mapped_column('email', String(96), nullable=False, index=True)
    telephone: Mapped[str] = mapped_column('telephone', String(32), nullable=False)
    password: Mapped[str] = mapped_column('password', String(255), nullable=False)
    custom_field: Mapped[str] = mapped_column('custom_field', Text, nullable=False)
    newsletter: Mapped[bool] = mapped_column('newsletter', Boolean, nullable=False)
    ip: Mapped[str] = mapped_column('ip', String(40), nullable=False)
    status: Mapped[bool] = mapped_column('status', Boolean, nullable=False)
    safe: Mapped[bool] = mapped_column('safe', Boolean, nullable=False)
    commenter: Mapped[bool] = mapped_column('commenter', Boolean, nullable=False)
    token: Mapped[str] = mapped_column('token', Text, nullable=False)
    code: Mapped[str] = mapped_column('code', String(40), nullable=False)
    date_added: Mapped[datetime] = mapped_column('date_added', DateTime, nullable=False)

    def __repr__(self) -> str:
        return f'<Customer id={self.customer_id}>'


class Cart(Base):
    __tablename__ = 'oc_cart'

    cart_id: Mapped[int] = mapped_column('cart_id', Integer, nullable=False, autoincrement=True,
                                         primary_key=True, unique=True, index=True)
    api_id: Mapped[int] = mapped_column('api_id', Integer, nullable=False, index=True)
    customer_id: Mapped[int] = mapped_column('customer_id', Integer,
                                             ForeignKey('oc_customer.customer_id'), nullable=False)
    session_id: Mapped[str] = mapped_column('session_id', String(32), nullable=False, index=True)
    product_id: Mapped[int] = mapped_column('product_id', Integer, nullable=False, index=True)
    subscription_plan_id: Mapped[int] = mapped_column('subscription_plan_id', Integer,
                                                      nullable=False, index=True)
    option: Mapped[str] = mapped_column('option', Text, nullable=False)
    quantity: Mapped[int] = mapped_column('quantity', Integer, nullable=False)
    override: Mapped[bool] = mapped_column('override', Boolean, nullable=False)
    price: Mapped[Decimal] = mapped_column('price', Numeric(15,4), nullable=False)
    date_added: Mapped[datetime] = mapped_column('date_added', DateTime, nullable=False)

    def __repr__(self) -> str:
        return f'<Cart id={self.cart_id}>'


class Product(Base):
    __tablename__ = 'oc_product'

    product_id: Mapped[int] = mapped_column('product_id', Integer, nullable=False,
                                            autoincrement=True, primary_key=True, unique=True, index=True)
    master_id: Mapped[int] = mapped_column('master_id', Integer, nullable=False, default=0)
    model: Mapped[str] = mapped_column('model', String(64), nullable=False)
    sku: Mapped[str] = mapped_column('sku', String(64), nullable=False)
    upc: Mapped[str] = mapped_column('upc', String(12), nullable=False)
    ean: Mapped[str] = mapped_column('ean', String(14), nullable=False)
    jan: Mapped[str] = mapped_column('jan', String(13), nullable=False)
    isbn: Mapped[str] = mapped_column('isbn', String(17), nullable=False)
    mpn: Mapped[str] = mapped_column('mpn', String(64), nullable=False)
    location: Mapped[str] = mapped_column('location', String(128), nullable=False)
    variant: Mapped[str] = mapped_column('variant', Text, nullable=False, default='')
    override: Mapped[str] = mapped_column('override', Text, nullable=False, default='')
    quantity: Mapped[int] = mapped_column('quantity', Integer, nullable=False, default=0)
    stock_status_id: Mapped[int] = mapped_column('stock_status_id', Integer, nullable=False)
    image: Mapped[str] = mapped_column('image', String(255), nullable=False)
    manufacturer_id: Mapped[int] = mapped_column('manufacturer_id', Integer, nullable=False)
    shipping: Mapped[bool] = mapped_column('shipping', Boolean, nullable=False, default=True)
    price: Mapped[Decimal] = mapped_column('price', Numeric(15,4), nullable=False,
                                           default=0)
    points: Mapped[int] = mapped_column('points', Integer, nullable=False, default=0)
    tax_class_id: Mapped[int] = mapped_column('tax_class_id', Integer, nullable=False)
    date_available: Mapped[datetime] = mapped_column('date_available', DateTime, nullable=False)
    weight: Mapped[Decimal] = mapped_column('weight', Numeric(15,8), nullable=False,
                                            default=0)
    weight_class_id: Mapped[int] = mapped_column('weight_class_id', Integer, nullable=False,
                                                 default=0)
    length: Mapped[Decimal] = mapped_column('length', Numeric(15,8), nullable=False,
                                            default=0)
    width: Mapped[Decimal] = mapped_column('width', Numeric(15,8), nullable=False,
                                           default=0)
    height: Mapped[Decimal] = mapped_column('height', Numeric(15,8), nullable=False,
                                            default=0)
    length_class_id: Mapped[int] = mapped_column('length_class_id', Integer, nullable=False,
                                                 default=0)
    subtract: Mapped[bool] = mapped_column('subtract', Boolean, nullable=False, default=True)
    minimum: Mapped[int] = mapped_column('minimum', Integer, nullable=False, default=1)
    rating: Mapped[bool] = mapped_column('rating', Boolean, nullable=False)
    sort_order: Mapped[int] = mapped_column('sort_order', Integer, nullable=False, default=0)
    status: Mapped[bool] = mapped_column('status', Boolean, nullable=False, default=False)
    date_added: Mapped[datetime] = mapped_column('date_added', DateTime, nullable=False)
    date_modified: Mapped[datetime] = mapped_column('date_modified', DateTime, nullable=False)

    def __repr__(self) -> str:
        return f'<Product id={self.product_id}>'


class ProductDescription(Base):
    __tablename__ = 'oc_product_description'

    product_id: Mapped[int] = mapped_column('product_id', Integer, nullable=False, primary_key=True,
                                            unique=True, index=True)
    language_id: Mapped[int] = mapped_column('language_id', Integer, nullable=False,
                                             primary_key=True, unique=True, index=True)
    name: Mapped[str] = mapped_column('name', String(255), nullable=False, index=True)
    description: Mapped[str] = mapped_column('description', Text, nullable=False)
    tag: Mapped[str] = mapped_column('tag', Text, nullable=False)
    meta_title: Mapped[str] = mapped_column('meta_title', String(255), nullable=False, index=True)
    meta_description: Mapped[str] = mapped_column('meta_description', String(255), nullable=False,
                                                  index=True)
    meta_keyword: Mapped[str] = mapped_column('meta_keyword', String(255), nullable=False,
                                              index=True)

    def __repr__(self) -> str:
        return f'<ProductDescription for id={self.product_id}>'
