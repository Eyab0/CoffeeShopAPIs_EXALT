from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.models import *
from marshmallow_sqlalchemy.fields import Nested


class EmployeeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        include_fk = True
        load_instance = True


class ItemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        include_relationships = True
        load_instance = True
        include_fk = True


class CustomerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        include_relationships = True
        load_instance = True
        include_fk = True


class OrderItemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = OrderItem
        include_relationships = True
        load_instance = True
        include_fk = True


class OrderSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        include_fk = True
        load_instance = True

    items_ordered = Nested(OrderItemSchema(only=("item_id", "quantity", "description"), many=True), many=True)


class BillSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Bill
        include_relationships = True
        load_instance = True
        include_fk = True
