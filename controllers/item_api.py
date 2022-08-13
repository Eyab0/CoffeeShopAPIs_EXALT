from flask import jsonify, request
from models.models import Item
from schemas.schemas import ItemSchema
from database import init_db as db
from custom_exceptions.HTTPRequestError import HTTPRequestError


def get_items():
    """
    get JSON info of all items
    :return: all items info
    """

    with db.session_scope() as s:
        item = s.query(Item).all()
        item_schema = ItemSchema()
        result = item_schema.dump(item, many=True)
        return jsonify(result), 200


def show_item_info(item_id: int):
    """
    show the JSON info for a specific item
    :param item_id:
    :return:
    """
    try:
        with db.session_scope() as s:
            item = s.query(Item).get(item_id)
            if item is None:
                raise HTTPRequestError(msg=f" id {item_id} Not Found !!", code=404)
            item_schema = ItemSchema()
            result = item_schema.dump(item)
            return jsonify(result), 200
    except HTTPRequestError as error:
        return {
                   "error": str(error.msg)
               }, error.code
    except Exception as error:
        return {
                   "error": str(error)
               }, 400


def insert_new_item():
    """
    insert new item into JSON file
    :return:
    """

    try:
        item = ItemSchema().load(request.json, transient=True)
        with db.session_scope() as s:
            s.add(item)
        item_schema = ItemSchema()
        new_item = item_schema.dump(item)
        return {
                   "message": "Created new item.",
                   "item": new_item
               }, 201

    except Exception as error:
        return {
                   "error": str(error)
               }, 400


def update_item_info(item_id: int):
    """
    update the item info
    :param item_id: id of the item
    :return: the updated info of the item
    """
    try:
        with db.session_scope() as s:
            item = s.query(Item).get(item_id)
            if item is None:
                raise HTTPRequestError(msg=f" id {item_id} Not Found !!", code=404)
            request.json["id"] = item_id
            item_schema = ItemSchema()
            existing_item_deserialized = item_schema.load(request.json, session=db.sess)
            s.merge(existing_item_deserialized)
            new_item_serialize = item_schema.dump(existing_item_deserialized)
            return {
                       "message": f"item with id :{item_id} Updated successfully",
                       "item": new_item_serialize
                   }, 200
    except HTTPRequestError as error:
        return {
                   "error": str(error.msg)
               }, error.code
    except Exception as error:
        return {
                   "error": str(error)
               }, 400


def delete_item(item_id: int):
    """
    delete specific item
    :param item_id: the id of the item
    :return: all items info
    """
    try:
        with db.session_scope() as s:
            item = s.query(Item).get(item_id)
            if item is None:
                raise HTTPRequestError(msg=f" id {item_id} Not Found !!", code=404)
            deleted_id = item.id
            s.delete(item)
            return {"message": f"item with id :{deleted_id} deleted successfully"}, 200
    except HTTPRequestError as error:
        return {
                   "error": str(error.msg)
               }, error.code
    except Exception as error:
        return {
                   "error": str(error)
               }, 400
