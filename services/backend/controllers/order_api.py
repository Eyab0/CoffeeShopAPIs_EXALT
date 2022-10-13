from services.backend.models.models import Order
from services.backend.schemas.schemas import OrderSchema
from services.backend.controllers import utils

api_type = "order"


def get_orders():
    """
    get JSON info of all orders
    :return: all orders info
    """
    return utils.get_objects(model=Order, schema=OrderSchema())


def show_order_info(order_id: int):
    """
    show the JSON info for a specific order
    :param order_id:
    :return:
    """
    return utils.show_object_info(object_id=order_id, model=Order, schema=OrderSchema())


def insert_new_order():
    """
    insert new order into JSON file
    :return:
    """

    return utils.insert_new_object(schema=OrderSchema(), controller_type=api_type)


def update_order_info(order_id: int):
    """
    update the order info
    :param order_id: id of the order
    :return: the updated info of the order
    """
    return utils.update_object_info(object_id=order_id, model=Order, schema=OrderSchema(), controller_type=api_type)


def delete_order_info(order_id: int):
    """
    delete specific order
    :param order_id: the id of the order
    :return: all orders info
    """
    return utils.delete_object_info(object_id=order_id, model=Order, controller_type=api_type)
