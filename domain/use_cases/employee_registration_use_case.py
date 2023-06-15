from entities.models.employee import *
from domain.getaways.db_gateway.operations.employee_db_operation import insert_employee
from entities.constants.regex import *
from werkzeug.security import generate_password_hash
from domain.utils.validation_utils import is_valid_string_input
import json


def employee_registration_use_case(emp_db, operation=insert_employee):
    if not is_valid_string_input(emp_db[EMPLOYEE_PASSWORD], PASSWORD_REGEX):
        raise Exception("Invalid password")
    if not is_valid_string_input(emp_db[EMPLOYEE_PHONE], EGYPTIAL_PHONE_NUMBER_REGEX):
        raise Exception("Invalid phone number")
    if not is_valid_string_input(emp_db[EMPLOYEE_EMAIL], EMAIL_ADDRESS_REGEX):
        raise Exception("Invalid email address")
    if not is_valid_string_input(emp_db[EMPLOYEE_NAME]):
        raise Exception("Name field is mandatory")
    if not is_valid_string_input(emp_db[EMPLOYEE_TITLE]):
        raise Exception("Title field is mandatory")
    hashed_password = generate_password_hash(emp_db[EMPLOYEE_PASSWORD])
    emp_db.update({EMPLOYEE_PASSWORD: hashed_password})
    return operation(emp_db)