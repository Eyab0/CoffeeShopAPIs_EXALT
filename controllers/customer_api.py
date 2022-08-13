from flask import jsonify, request
from models.models import Customer
from schemas.schemas import CustomerSchema
from database import init_db as db
from custom_exceptions.HTTPRequestError import HTTPRequestError


def get_customers():
    """
    get JSON info of all customers
    :return: all customers info
    """

    with db.session_scope() as s:
        customer = s.query(Customer).all()
        customer_schema = CustomerSchema()
        result = customer_schema.dump(customer, many=True)
        return jsonify(result), 200


def show_customer_info(customer_id: int):
    """
    show the JSON info for a specific customer
    :param customer_id:
    :return:
    """
    try:
        with db.session_scope() as s:
            customer = s.query(Customer).get(customer_id)
            if customer is None:
                raise HTTPRequestError(msg=f" id {customer_id} Not Found !!", code=404)
            customer_schema = CustomerSchema()
            result = customer_schema.dump(customer)
            return jsonify(result), 200
    except HTTPRequestError as error:
        return {
                   "error": str(error.msg)
               }, error.code
    except Exception as error:
        return {
                   "error": str(error)
               }, 400


def insert_new_customer():
    """
    insert new customer into JSON file
    :return:
    """

    try:
        customer = CustomerSchema().load(request.json, transient=True)
        with db.session_scope() as s:
            s.add(customer)
        customer_schema = CustomerSchema()
        new_customer = customer_schema.dump(customer)
        return {
                   "message": "Created new customer.",
                   "customer": new_customer
               }, 201

    except Exception as error:
        return {
                   "error": str(error)
               }, 400


def update_customer_info(customer_id: int):
    """
    update the customer info
    :param customer_id: id of the customer
    :return: the updated info of the customer
    """
    try:
        with db.session_scope() as s:
            customer = s.query(Customer).get(customer_id)
            if customer is None:
                raise HTTPRequestError(msg=f" id {customer_id} Not Found !!", code=404)
            request.json["id"] = customer_id
            customer_schema = CustomerSchema()
            existing_customer_deserialized = customer_schema.load(request.json, session=db.sess)
            s.merge(existing_customer_deserialized)
            new_customer_serialize = customer_schema.dump(existing_customer_deserialized)
            return {
                       "message": f"customer with id :{customer_id} Updated successfully",
                       "customer": new_customer_serialize
                   }, 200
    except HTTPRequestError as error:
        return {
                   "error": str(error.msg)
               }, error.code
    except Exception as error:
        return {
                   "error": str(error)
               }, 400



