from datetime import datetime, date
from flask import jsonify, request
from models.models import *
from schemas.schemas import EmployeeSchema
from database import init_db as db

# emp = Employee(
#     name='eyab',
#     address='palestine',
#     phone_number='0509232990',
#     date_of_birth=date(2000, 11, 11),
#     role='cash'
#
# )
# cus = Customer(
#     name='abod',
# )
#
# itm = Item(
#     name='coffee',
#     cost=12.5
# )
# with db.session_scope() as s:
#     s.add(emp)

# with db.session_scope() as s:
#     s.add(cus)
#
# with db.session_scope() as s:
#     s.add(itm)

ord = OrderItem(
    order_id=1,
    item_id=1,
    quantity=1
)

with db.session_scope() as s:
    s.add(ord)

# with db.session_scope() as s:
#     s.add(emp)
