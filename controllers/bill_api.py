from flask import jsonify, request
from models.models import Bill
from schemas.schemas import BillSchema
from database import init_db as db
from custom_exceptions.HTTPRequestError import HTTPRequestError


def get_bills():
    """
    get JSON info of all bills
    :return: all bills info
    """

    with db.session_scope() as s:
        bill = s.query(Bill).all()
        bill_schema = BillSchema()
        result = bill_schema.dump(bill, many=True)
        return jsonify(result), 200


def show_bill_info(bill_id: int):
    """
    show the JSON info for a specific bill
    :param bill_id:
    :return:
    """
    try:
        with db.session_scope() as s:
            bill = s.query(Bill).get(bill_id)
            if bill is None:
                raise HTTPRequestError(msg=f" id {bill_id} Not Found !!", code=404)
            bill_schema = BillSchema()
            result = bill_schema.dump(bill)
            return jsonify(result), 200
    except HTTPRequestError as error:
        return {
                   "error": str(error.msg)
               }, error.code
    except Exception as error:
        return {
                   "error": str(error)
               }, 400


def insert_new_bill():
    """
    insert new bill into JSON file
    :return:
    """

    try:
        bill = BillSchema().load(request.json, transient=True)
        with db.session_scope() as s:
            s.add(bill)
        bill_schema = BillSchema()
        new_bill = bill_schema.dump(bill)
        return {
                   "message": "Created new bill.",
                   "bill": new_bill
               }, 201

    except Exception as error:
        return {
                   "error": str(error)
               }, 400


def update_bill_info(bill_id: int):
    """
    update the bill info
    :param bill_id: id of the bill
    :return: the updated info of the bill
    """
    try:
        with db.session_scope() as s:
            bill = s.query(Bill).get(bill_id)
            if bill is None:
                raise HTTPRequestError(msg=f" id {bill_id} Not Found !!", code=404)
            request.json["id"] = bill_id
            bill_schema = BillSchema()
            existing_bill_deserialized = bill_schema.load(request.json, session=db.sess)
            s.merge(existing_bill_deserialized)
            new_bill_serialize = bill_schema.dump(existing_bill_deserialized)
            return {
                       "message": f"bill with id :{bill_id} Updated successfully",
                       "bill": new_bill_serialize
                   }, 200
    except HTTPRequestError as error:
        return {
                   "error": str(error.msg)
               }, error.code
    except Exception as error:
        return {
                   "error": str(error)
               }, 400


def delete_bill_info(bill_id: int):
    """
    delete specific bill
    :param bill_id: the id of the bill
    :return: all bills info
    """
    try:
        with db.session_scope() as s:
            bill = s.query(Bill).get(bill_id)
            if bill is None:
                raise HTTPRequestError(msg=f" id {bill_id} Not Found !!", code=404)
            deleted_id = bill.id
            s.delete(bill)
            return {"message": f"bill with id :{deleted_id} deleted successfully"}, 200
    except HTTPRequestError as error:
        return {
                   "error": str(error.msg)
               }, error.code
    except Exception as error:
        return {
                   "error": str(error)
               }, 400
