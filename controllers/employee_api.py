from flask import jsonify, request
from models.models import Employee
from schemas.schemas import EmployeeSchema
from database import init_db as db
from custom_exceptions.HTTPRequestError import HTTPRequestError


def get_employees():
    """
    get JSON info of all employees
    :return: all employees info
    """

    with db.session_scope() as s:
        employee = s.query(Employee).all()
        employee_schema = EmployeeSchema()
        result = employee_schema.dump(employee, many=True)
        return jsonify(result), 200


def show_employee_info(emp_id: int):
    """
    show the JSON info for a specific employee
    :param emp_id:
    :return:
    """
    try:
        with db.session_scope() as s:
            employee = s.query(Employee).get(emp_id)
            if employee is None:
                raise HTTPRequestError(msg=f" id {emp_id} Not Found !!", code=404)
            employee_schema = EmployeeSchema()
            result = employee_schema.dump(employee)
            return jsonify(result), 200
    except HTTPRequestError as error:
        return {
                   "error": str(error.msg)
               }, error.code
    except Exception as error:
        return {
                   "error": str(error)
               }, 400


def insert_new_employee():
    """
    insert new employee into JSON file
    :return:
    """

    try:
        employee = EmployeeSchema().load(request.json, transient=True)
        with db.session_scope() as s:
            s.add(employee)
        employee_schema = EmployeeSchema()
        new_employee = employee_schema.dump(employee)
        return {
                   "message": "Created new employee.",
                   "employee": new_employee
               }, 201

    except Exception as error:
        return {
                   "error": str(error)
               }, 400


def update_employee_info(emp_id: int):
    """
    update the employee info
    :param emp_id: id of the employee
    :return: the updated info of the employee
    """
    try:
        with db.session_scope() as s:
            employee = s.query(Employee).get(emp_id)
            if employee is None:
                raise HTTPRequestError(msg=f" id {emp_id} Not Found !!", code=404)
            request.json["id"] = emp_id
            employee_schema = EmployeeSchema()
            existing_employee_deserialized = employee_schema.load(request.json, session=db.sess)
            s.merge(existing_employee_deserialized)
            new_employee_serialize = employee_schema.dump(existing_employee_deserialized)
            return {
                       "message": f"employee with id :{emp_id} Updated successfully",
                       "employee": new_employee_serialize
                   }, 200
    except HTTPRequestError as error:
        return {
                   "error": str(error.msg)
               }, error.code
    except Exception as error:
        return {
                   "error": str(error)
               }, 400
