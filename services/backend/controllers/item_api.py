from services.backend.models.models import Item
from services.backend.schemas.schemas import ItemSchema
from services.backend.controllers import utils

api_type = "item"


def get_items():
    """
    get JSON info of all items
    :return: all items info
    """

    return utils.get_objects(model=Item, schema=ItemSchema())


def show_item_info(item_id: int):
    """
    show the JSON info for a specific item
    :param item_id:
    :return:
    """
    return utils.show_object_info(object_id=item_id, model=Item, schema=ItemSchema())


def insert_new_item():
    """
    insert new item into JSON file
    :return:
    """

    return utils.insert_new_object(schema=ItemSchema(), controller_type=api_type)


def update_item_info(item_id: int):
    """
    update the item info
    :param item_id: id of the item
    :return: the updated info of the item
    """
    return utils.update_object_info(object_id=item_id, model=Item, schema=ItemSchema(), controller_type=api_type)


def delete_item_info(item_id: int):
    """
    delete specific item
    :param item_id: the id of the item
    :return: all items info
    """
    return utils.delete_object_info(object_id=item_id, model=Item, controller_type=api_type)
