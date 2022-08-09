from datetime import datetime

from sqlalchemy import UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sqlalchemy as sa

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employee"
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    phone_number = sa.Column(sa.String, nullable=False)
    date_of_birth = sa.Column(sa.DATE, nullable=False)
    address = sa.Column(sa.String, nullable=True)
    join_date = sa.Column(sa.DATE, nullable=False, default=datetime.now().strftime("%Y-%m-%d"))
    role = sa.Column(sa.String, nullable=False)
    UniqueConstraint(phone_number)

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "


class Order(Base):
    __tablename__ = "order"
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer, primary_key=True)

    employee_id = sa.Column(sa.Integer, sa.ForeignKey("employee.id"))
    employee = relationship(Employee, back_populates="employee")

    customer_id = sa.Column(sa.Integer, sa.ForeignKey("customer.id"))
    customer = relationship(Employee, back_populates="customer")

    items_ordered = relationship("orderItem", back_populates="order", cascade="all, delete",
                                 passive_deletes=True)

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "


class Item(Base):
    __tablename__ = "item"
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    cost = sa.Column(sa.Float, nullable=False)

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "


class Customer(Base):
    __tablename__ = "customer"
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=True)
    phone_number = sa.Column(sa.String, nullable=True)

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "


class OrderItem(Base):
    __tablename__ = "orderItem "
    __table_args__ = {'extend_existing': True}

    order_id = sa.Column(sa.Integer, sa.ForeignKey("order.id", ondelete="CASCADE"), primary_key=True)
    item_id = sa.Column(sa.Integer, sa.ForeignKey("item.id", ondelete="CASCADE"), nullable=False)
    quantity = sa.Column(sa.Integer, nullable=False)
    description = sa.Column(sa.String, nullable=True)
    order = relationship(Order, back_populates="orderItem")
    item = relationship(Item, back_populates="orderItem")

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "

# class Bill(Base):
#     __tablename__ = "Bill"
#     __table_args__ = {'extend_existing': True}
#
#     order_id = sa.Column(sa.Integer, sa.ForeignKey("Order.id", ondelete="CASCADE"), primary_key=True)
#     total_cost = sa.Column(sa.Float, nullable=False)
#     # order_time = sa.Column(sa.DATETIME, nullable=False, default=datetime.utcnow)
#     description = sa.Column(sa.String, nullable=False)
#     employee_id = sa.Column(sa.Integer, sa.ForeignKey("Employee.id"))
#     customer_id = sa.Column(sa.Integer, sa.ForeignKey("Customer.id"))
#
#     order = relationship(Order, back_populates="Bill", uselist=False, cascade="all, delete",
#                          passive_deletes=True)
#     employee = relationship(Employee, back_populates="Bill")
#     customer = relationship(Customer, back_populates="Bill")
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "
