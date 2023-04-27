from entities.models.employee import *
from domain.getaways.db_gateway.operations.employee_db_operation import retrieve_employee_by_email
from entities.constants.regex import *
from werkzeug.security import check_password_hash
from domain.utils.validation_utils import is_valid_string_input


def invalid_login_credentials():
    return Exception("Invalid email, or password")


def employee_login_use_case(email, password, operation=retrieve_employee_by_email):
    if not is_valid_string_input(email, EMAIL_ADDRESS_REGEX) or not is_valid_string_input(password, PASSWORD_REGEX):
        raise invalid_login_credentials()
    employee = operation(email)
    if employee is None or check_password_hash(employee[EMPLOYEE_PASSWORD], password):
        raise invalid_login_credentials()
    return employee
