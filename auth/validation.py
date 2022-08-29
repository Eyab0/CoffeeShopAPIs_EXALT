from flask import request
from config import config
from jwt import decode


def validate_token():
    """
    :return: the status of the access token
    """
    # no need for access access_token if the employee is logining
    if not config.ROLES.get(str(request.url_rule)):
        return None

    # check if the access access_token is exists
    access_token_header = request.headers.get("Authorization")
    if not access_token_header:
        return {
                   "error": "access access_token not found !"
               }, 400

    access_token = access_token_header.split(" ")[1].strip()
    access_token_decoded = decode_access_token(access_token)
    is_allowed = check_operation(str(request.url_rule), access_token_decoded)
    if not is_allowed:
        return {
                   "error": "Employee Unauthorized !"
               }, 401


def check_operation(endpoint_path, access_token):
    """
    This method checks if an employee is allowed to access this API Endpoint
    :param endpoint_path: API Endpoint
    :param access_token: Decoded access token
    :return: True if is allowed , False otherwise
    """
    role = access_token.get("role")
    if role in config.ROLES.get(endpoint_path):
        return True
    return False


def decode_access_token(access_token):
    """

    :param access_token:
    :return: payload Dict
    """
    return decode(access_token, config.PUBLIC_KEY, algorithms=config.ALGORITHM)
