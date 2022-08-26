from datetime import datetime
from bcrypt import checkpw, hashpw, gensalt
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary, DATE, Float, TIMESTAMP

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employee"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True)
    date_of_birth = Column(DATE, nullable=False)
    address = Column(String, nullable=True)
    join_date = Column(DATE, nullable=False, default=datetime.now().strftime("%Y-%m-%d"))
    role = Column(String, nullable=False)
    status = Column(String, nullable=True, default='Active')
    orders_served = relationship('Order', back_populates='employee')
    username = Column(String, unique=True)
    password = Column(LargeBinary)

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "


class Item(Base):
    __tablename__ = "item"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cost = Column(Float, nullable=False)
    item_ordered = relationship('OrderItem', back_populates='item_details')

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "


class Customer(Base):
    __tablename__ = "customer"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True, default='Customer')
    phone_number = Column(String, nullable=True, default='no Phone Number')
    orders_placed = relationship('Order', back_populates='customer')

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "


class Order(Base):
    __tablename__ = "order"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("employee.id"))
    employee = relationship(Employee, back_populates="orders_served")
    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship(Customer, back_populates="orders_placed")
    status = Column(String, nullable=False, default='in Progress')
    items_ordered = relationship("OrderItem", back_populates="order", cascade="all, delete",
                                 passive_deletes=True)

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "


class OrderItem(Base):
    __tablename__ = "orderItem "
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("order.id", ondelete="CASCADE"), nullable=True)
    item_id = Column(Integer, ForeignKey("item.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    order = relationship('Order', back_populates="items_ordered")
    item_details = relationship('Item', back_populates="item_ordered")

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "


class Bill(Base):
    __tablename__ = "Bill"
    __table_args__ = {'extend_existing': True}

    order_id = Column(Integer, ForeignKey("order.id"), primary_key=True)
    total_cost = Column(Float, nullable=False)
    order_time = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    employee_id = Column(Integer, ForeignKey("employee.id"))
    customer_id = Column(Integer, ForeignKey("customer.id"), nullable=True)

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v!r}' for k, v in self.__dict__.items() if not k.startswith('_')])}) "
