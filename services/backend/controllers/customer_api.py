from services.backend.models.models import Customer
from services.backend.schemas.schemas import CustomerSchema
from services.backend.controllers import utils

api_type = "customer"


def get_customers():
    """
    get JSON info of all customers
    :return: all customers info
    """

    return utils.get_objects(model=Customer, schema=CustomerSchema())


def show_customer_info(customer_id: int):
    """
    show the JSON info for a specific customer
    :param customer_id:
    :return:
    """
    return utils.show_object_info(object_id=customer_id, model=Customer, schema=CustomerSchema())


def insert_new_customer():
    """
    insert new customer into JSON file
    :return:
    """

    return utils.insert_new_object(schema=CustomerSchema(), controller_type=api_type)


def update_customer_info(customer_id: int):
    """
    update the customer info
    :param customer_id: id of the customer
    :return: the updated info of the customer
    """
    return utils.update_object_info(object_id=customer_id, model=Customer, schema=CustomerSchema(),
                                    controller_type=api_type)
