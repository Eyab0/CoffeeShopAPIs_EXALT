from datetime import datetime

from sqlalchemy import UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sqlalchemy as sa

Base = declarative_base()


class Emp(Base):
    __tablename__ = "Emp"
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    phone_number = sa.Column(sa.String, nullable=False)
    date_of_birth = sa.Column(sa.DATE, nullable=False)
    address = sa.Column(sa.String, nullable=True)
    city = sa.Column(sa.String, nullable=False)
    date = datetime.year, '-', datetime.month, '-', datetime.day
    join_date = sa.Column(sa.DATE, nullable=False, default=date)
    role = sa.Column(sa.String, nullable=False)
    UniqueConstraint(phone_number)

    #
    # address = relationship("Address", back_populates="user", uselist=False, cascade="all, delete",
    #                        passive_deletes=True)
    #
    # phone_numbers = relationship("PhoneNumbers", back_populates="user", cascade="all, delete",
    #                              passive_deletes=True)

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "


class Order(Base):
    __tablename__ = "Order"
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer, primary_key=True)
    date_time = sa.Column(sa.DATETIME, nullable=False, default=datetime.utcnow)
    description = sa.Column(sa.String, nullable=False)

    emp_id = sa.Column(sa.Integer, sa.ForeignKey("Emp.id", ondelete="CASCADE"))
    emp = relationship(Emp, back_populates="Emp")

    customer_id = sa.Column(sa.Integer, sa.ForeignKey("Customer.id", ondelete="CASCADE"))
    customer = relationship(Emp, back_populates="Customer")

    order_of_items = relationship("OrderOfItems", back_populates="Order", cascade="all, delete",
                                  passive_deletes=True)

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "


class Item(Base):
    __tablename__ = "Item"
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    cost = sa.Column(sa.Float, nullable=False)

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "


class Customer(Base):
    __tablename__ = "Customer"
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=True)
    phone_number = sa.Column(sa.String, nullable=True)

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "


class OrderOfItems(Base):
    __tablename__ = "OrderOfItems"
    __table_args__ = {'extend_existing': True}

    order_id = sa.Column(sa.Integer, sa.ForeignKey("Order.id", ondelete="CASCADE"), primary_key=True)
    item_id = sa.Column(sa.String, sa.ForeignKey("Item.id", ondelete="CASCADE"), nullable=False)
    quantity = sa.Column(sa.Integer, nullable=False)
    description = sa.Column(sa.String, nullable=False)

    order = relationship(Order, back_populates="OrderOfItems")
    item = relationship(Item, back_populates="OrderOfItems")

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "


class Bill(Base):
    __tablename__ = "Bill"
    __table_args__ = {'extend_existing': True}

    order_id = sa.Column(sa.Integer, sa.ForeignKey("Order.id", ondelete="CASCADE"), primary_key=True)
    total_cost = sa.Column(sa.Float, nullable=False)
    date_time = sa.Column(sa.DATETIME, nullable=False, default=datetime.utcnow)
    description = sa.Column(sa.String, nullable=False)
    by_emp = sa.Column(sa.Integer, sa.ForeignKey("Emp.id", ondelete="CASCADE"))
    for_customer = sa.Column(sa.Integer, sa.ForeignKey("Customer.id", ondelete="CASCADE"))

    order = relationship(Order, back_populates="Bill")
    emp = relationship(Emp, back_populates="Bill")
    customer = relationship(Customer, back_populates="Bill")

    order_of_items = relationship("Order", back_populates="Bill", uselist=False, cascade="all, delete",
                                  passive_deletes=True)

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "
