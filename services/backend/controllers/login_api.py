from services.backend.models.models import Employee
from flask import request
from services.backend.database import init_db as db
from services.backend.auth import access_token


def employee_login():
    """

    :return: access access_token
    """

    employee = db.sess.query(Employee).filter(Employee.username == request.json['username']).one_or_none()

    if not employee or not employee.check_password(request.json['password']):
        return {
                   "error": "password or username incorrect"
               }, 404

    # generate access access_token
    return {
               "access_token": access_token.generate_access_token(employee)
           }, 200
