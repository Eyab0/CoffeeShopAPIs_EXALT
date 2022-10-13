import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

HOST = os.getenv("HOST")
DBNAME = os.getenv("DBNAME")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
ALGORITHM = os.getenv("ALGORITHM")

PRIVATE_KEY = open("jwt-key").read()
PUBLIC_KEY = open("jwt-key.pub").read()

# manager : all operations
# warehouse : items only
# cashier : items & customer & order & bill
# barista : orders only
ROLES = {
    "/shop/item": ["warehouse", "cashier", "manager"],
    "/shop/item/<int:order_id>": ["warehouse", "cashier", "manager"],
    "/shop/customer": ["cashier", "manager"],
    "/shop/customer/<int:customer_id>": ["cashier", "manager"],
    "/shop/order": ["barista", "cashier", "manager"],
    "/shop/order/<int:order_id>": ["barista", "cashier", "manager"],
    "/shop/bill": ["cashier", "manager"],
    "/shop/bill/<int:order_id>": ["cashier", "manager"],

    "/manager/employee": ["manager"],
    "/manager/employee/<int:employee_id>": ["manager"],

    "/auth/login": None,
}
