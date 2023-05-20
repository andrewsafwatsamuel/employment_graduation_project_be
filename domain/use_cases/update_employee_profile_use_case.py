from domain.getaways.db_gateway.operations.employee_db_operation import update_emp_profile
from domain.utils.validation_utils import is_valid_string_input
from entities.constants.regex import *
from entities.models.employee import *


def update_employee_profile_use_case(employee_db, operation=update_emp_profile):
    if employee_db[EMPLOYEE_ID] is None:
        raise Exception("Invalid data")
    if not is_valid_string_input(employee_db[EMPLOYEE_ID]):
        raise Exception("User name must not be null or blank")
    if not is_valid_string_input(employee_db[EMPLOYEE_PHONE], EGYPTIAL_PHONE_NUMBER_REGEX):
        raise Exception("Invalid phone number")
    if not is_valid_string_input(employee_db[EMPLOYEE_EMAIL], EMAIL_ADDRESS_REGEX):
        raise Exception("Invalid Email")
    if not is_valid_string_input(employee_db[EMPLOYEE_TITLE]):
        raise Exception("Title must not be null or blank")
    return operation(employee_db) > 0
