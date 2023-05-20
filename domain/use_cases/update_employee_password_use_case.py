from entities.models.employee import *
from domain.getaways.db_gateway.operations.employee_db_operation import retrieve_employee_by_email, update_emp_password
from entities.constants.regex import *
from werkzeug.security import check_password_hash
from domain.utils.validation_utils import is_valid_string_input


def update_password_use_case(
        email,
        old_password,
        new_password,
        retrieve_emp_operation=retrieve_employee_by_email,
        update_password_operation=update_emp_password
):
    if not is_valid_string_input(email, EMAIL_ADDRESS_REGEX) or not is_valid_string_input(old_password, PASSWORD_REGEX):
        raise Exception("Error has occurred")
    employee = retrieve_emp_operation(email)
    if employee is None or not check_password_hash(employee[EMPLOYEE_PASSWORD], old_password):
        raise Exception("Error has occurred")
    return update_password_operation(employee[EMPLOYEE_ID], new_password) > 0
