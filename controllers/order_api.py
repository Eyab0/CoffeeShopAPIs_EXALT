from flask import jsonify, request
from models.models import Order
from schemas.schemas import OrderSchema
from database import init_db as db
from custom_exceptions.HTTPRequestError import HTTPRequestError


def get_orders():
    """
    get JSON info of all orders
    :return: all orders info
    """

    with db.session_scope() as s:
        order = s.query(Order).all()
        order_schema = OrderSchema()
        result = order_schema.dump(order, many=True)
        return jsonify(result), 200


def show_order_info(order_id: int):
    """
    show the JSON info for a specific order
    :param order_id:
    :return:
    """
    try:
        with db.session_scope() as s:
            order = s.query(Order).get(order_id)
            if order is None:
                raise HTTPRequestError(msg=f" id {order_id} Not Found !!", code=404)
            order_schema = OrderSchema()
            result = order_schema.dump(order)
            return jsonify(result), 200
    except HTTPRequestError as error:
        return {
                   "error": str(error.msg)
               }, error.code
    except Exception as error:
        return {
                   "error": str(error)
               }, 400


def insert_new_order():
    """
    insert new order into JSON file
    :return:
    """

    try:
        order = OrderSchema().load(request.json, transient=True)
        with db.session_scope() as s:
            s.add(order)
        order_schema = OrderSchema()
        new_order = order_schema.dump(order)
        return {
                   "message": "Created new order.",
                   "order": new_order
               }, 201

    except Exception as error:
        return {
                   "error": str(error)
               }, 400


def update_order_info(order_id: int):
    """
    update the order info
    :param order_id: id of the order
    :return: the updated info of the order
    """
    try:
        with db.session_scope() as s:
            order = s.query(Order).get(order_id)
            if order is None:
                raise HTTPRequestError(msg=f" id {order_id} Not Found !!", code=404)
            request.json["id"] = order_id
            order_schema = OrderSchema()
            existing_order_deserialized = order_schema.load(request.json, session=db.sess)
            s.merge(existing_order_deserialized)
            new_order_serialize = order_schema.dump(existing_order_deserialized)
            return {
                       "message": f"order with id :{order_id} Updated successfully",
                       "order": new_order_serialize
                   }, 200
    except HTTPRequestError as error:
        return {
                   "error": str(error.msg)
               }, error.code
    except Exception as error:
        return {
                   "error": str(error)
               }, 400


def delete_order(order_id: int):
    """
    delete specific order
    :param order_id: the id of the order
    :return: all orders info
    """
    try:
        with db.session_scope() as s:
            order = s.query(OrderSchema).get(order_id)
            if order is None:
                raise HTTPRequestError(msg=f" id {order_id} Not Found !!", code=404)
            deleted_id = order.id
            s.delete(order)
            return {"message": f"order with id :{deleted_id} deleted successfully"}, 200
    except HTTPRequestError as error:
        return {
                   "error": str(error.msg)
               }, error.code
    except Exception as error:
        return {
                   "error": str(error)
               }, 400
