from models.models import Employee
from schemas.schemas import EmployeeSchema
from controllers import utils

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

    return utils.insert_new_object(schema=EmployeeSchema(), controller_type=api_type)


def update_employee_info(emp_id: int):
    """
    update the employee info
    :param emp_id: id of the employee
    :return: the updated info of the employee
    """
    return utils.update_object_info(object_id=emp_id, model=Employee, schema=EmployeeSchema(), controller_type=api_type)
