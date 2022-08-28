from models.models import Employee
from schemas.schemas import EmployeeSchema
from controllers import utils
from flask import request
from database import init_db as db

api_type = "employee"


def get_employees():
    """
    get JSON info of all employees
    :return: all employees info
    """

    return utils.get_objects(model=Employee, schema=EmployeeSchema())


def show_employee_info(emp_id: int):
    """
    show the JSON info for a specific employee
    :param emp_id:
    :return:
    """
    return utils.show_object_info(object_id=emp_id, model=Employee, schema=EmployeeSchema())


def insert_new_employee():
    """
    insert new employee into JSON file
    :return:
    """
    password = request.json["password"]
    employee_data = request.json
    employee_data.pop("password")
    try:
        # schema = EmployeeSchema()
        # _object = schema.load(employee_data, transient=True)
        # with db.session_scope() as s:
        #     s.add(_object)
        # new_object = schema.dump(_object)
        new_employee_deserialized = EmployeeSchema().load(employee_data, session=db.sess)
        # with db.session_scope() as s:
        db.sess.add(new_employee_deserialized)
        new_employee_deserialized.set_hash_password(password)
        db.sess.commit()
        result = EmployeeSchema().dump(new_employee_deserialized, many=False)
        print(new_employee_deserialized)
        print(type(new_employee_deserialized))
        return {
                   "message": f"Created new {api_type}.",
                   api_type: result
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
    return utils.update_object_info(object_id=emp_id, model=Employee, schema=EmployeeSchema(), controller_type=api_type)
