from flask import jsonify, request
from models.models import Bill
from schemas.schemas import BillSchema
from database import init_db as db
from custom_exceptions.HTTPRequestError import HTTPRequestError
from controllers import utils

api_type = "bill"


def get_bills():
    """
    get JSON info of all bills
    :return: all bills info
    """
    return utils.get_objects(model=Bill, schema=BillSchema())


def show_bill_info(order_id: int):
    """
    show the JSON info for a specific bill
    :param order_id:
    :return:
    """
    return utils.show_object_info(object_id=order_id, model=Bill, schema=BillSchema())


def insert_new_bill():
    """
    insert new bill into JSON file
    :return:
    """
    return utils.insert_new_object(schema=BillSchema(), controller_type=api_type)


def update_bill_info(order_id: int):
    """
    update the bill info
    :param order_id: id of the bill
    :return: the updated info of the bill
    """
    return utils.update_object_info(object_id=order_id, model=Bill, schema=BillSchema(), controller_type=api_type)


def delete_bill_info(order_id: int):
    """
    delete specific bill
    :param order_id: the id of the bill
    :return: all bills info
    """
    return utils.delete_object_info(object_id=order_id, model=Bill, controller_type=api_type)
