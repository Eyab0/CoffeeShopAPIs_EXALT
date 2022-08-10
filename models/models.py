from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sqlalchemy as sa

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employee"
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    phone_number = sa.Column(sa.String, nullable=False, unique=True)
    date_of_birth = sa.Column(sa.DATE, nullable=False)
    address = sa.Column(sa.String, nullable=True)
    join_date = sa.Column(sa.DATE, nullable=False, default=datetime.now().strftime("%Y-%m-%d"))
    role = sa.Column(sa.String, nullable=False)
    orders_served = relationship('Order', back_populates='employee')

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "


class Item(Base):
    __tablename__ = "item"
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    cost = sa.Column(sa.Float, nullable=False)

    item_ordered = relationship('OrderItem', back_populates='item_details')

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "


class Customer(Base):
    __tablename__ = "customer"
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=True)
    phone_number = sa.Column(sa.String, nullable=True)
    orders_placed = relationship('Order', back_populates='customer')

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "


class Order(Base):
    __tablename__ = "order"
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer, primary_key=True)

    employee_id = sa.Column(sa.Integer, sa.ForeignKey("employee.id"))
    employee = relationship(Employee, back_populates="orders_served")
    customer_id = sa.Column(sa.Integer, sa.ForeignKey("customer.id"))
    customer = relationship(Customer, back_populates="orders_placed")
    items_ordered = relationship("OrderItem", back_populates="order")

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "


class OrderItem(Base):
    __tablename__ = "orderItem "
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer, primary_key=True)
    order_id = sa.Column(sa.Integer, sa.ForeignKey("order.id"), nullable=False)
    item_id = sa.Column(sa.Integer, sa.ForeignKey("item.id"), nullable=False)
    quantity = sa.Column(sa.Integer, nullable=False)
    description = sa.Column(sa.String, nullable=True)
    order = relationship('Order', back_populates="items_ordered")
    item_details = relationship('Item', back_populates="item_ordered")

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "


class Bill(Base):
    __tablename__ = "Bill"
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer, primary_key=True)
    order_id = sa.Column(sa.Integer, sa.ForeignKey("order.id"))
    total_cost = sa.Column(sa.Float, nullable=False)
    order_time = sa.Column(sa.TIMESTAMP, nullable=False, default=datetime.utcnow)
    description = sa.Column(sa.String, nullable=True)
    employee_id = sa.Column(sa.Integer, sa.ForeignKey("employee.id"))
    customer_id = sa.Column(sa.Integer, sa.ForeignKey("customer.id"))

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "
