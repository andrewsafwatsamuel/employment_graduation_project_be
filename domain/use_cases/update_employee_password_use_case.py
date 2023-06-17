from entities.models.employee import *
from domain.getaways.db_gateway.operations.employee_db_operation import retrieve_employee_by_id, update_emp_password
from entities.constants.regex import *
from werkzeug.security import check_password_hash, generate_password_hash
from domain.utils.validation_utils import is_valid_string_input


def update_employee_password_use_case(
        emp_id,
        old_password,
        new_password,
        retrieve_emp_operation=retrieve_employee_by_id,
        update_password_operation=update_emp_password
):
    if emp_id is None or not is_valid_string_input(old_password):
        raise Exception("Invalid inputs")
    if not is_valid_string_input(new_password, PASSWORD_REGEX):
        raise Exception("Invalid new password")
    employee = retrieve_emp_operation(emp_id)
    if employee is None or not check_password_hash(employee[EMPLOYEE_PASSWORD], old_password):
        raise Exception("Invalid inputs")
    encrypted_password = generate_password_hash(new_password)
    return update_password_operation(employee[EMPLOYEE_ID], encrypted_password) > 0
