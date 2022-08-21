from models.models import Bill, Order, Item
from schemas.schemas import BillSchema, OrderSchema, ItemSchema
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


def generate_new_bill(order_id: int):
    """
    insert new bill into JSON file
    :return:
    """
    bill_info = {}
    total_cost = 0
    try:
        with db.session_scope() as s:
            order_object = s.query(Order).get(order_id)
            if order_object is None:
                raise HTTPRequestError(msg=f" id {order_id} Not Found !!", code=404)

            order_schema = OrderSchema()
            order = order_schema.dump(order_object)
            for item in order['items_ordered']:
                item_query = s.query(Item).get(item['item_id'])
                item_schema = ItemSchema()
                item_info = item_schema.dump(item_query)
                total_cost = total_cost + (item_info['cost'] * item['quantity'])
            bill_info['order_id'] = order_id
            bill_info['employee_id'] = order['employee_id']
            bill_info['customer_id'] = order['customer_id']
            bill_info['total_cost'] = total_cost

            bill_object = s.query(Bill).get(order_id)
            if bill_object is not None:
                bill_schema = BillSchema()
                existing_object_deserialized = bill_schema.load(bill_info, session=db.sess)
                s.merge(existing_object_deserialized)
                new_object_serialize = bill_schema.dump(existing_object_deserialized)
                return {
                           "message": f"Bill with id :{order_id} Updated successfully",
                           "Bill": new_object_serialize
                       }, 200

            bill = BillSchema().load(bill_info, transient=True)
            s.add(bill)
            bill_schema = BillSchema()
            new_bill = bill_schema.dump(bill)
            return {
                       "message": "Created new Bill.",
                       "Bill": new_bill
                   }, 201
    except HTTPRequestError as error:
        return {
                   "error": str(error.msg)
               }, error.code
    except Exception as error:
        return {
                   "error": str(error)
               }, 400


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
