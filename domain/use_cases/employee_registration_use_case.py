from entities.models.employee import *
from domain.getaways.db_gateway.operations.employee_db_operation import insert_employee
from entities.constants.regex import *
from werkzeug.security import generate_password_hash
from domain.utils.validation_utils import is_valid_string_input
import json


def employee_registration_use_case(emp_db, experiences, operation=insert_employee):
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
    return operation(emp_db, __exp_to_json_array(experiences))


def __exp_to_json_array(experiences):
    result = []
    for experience in experiences:
        if not is_valid_string_input(experience, VALID_JSON_OBJECT_REGEX):
            continue
        try:
            data = json.loads(experience)
            if data.keys() == {EXPERIENCE_EMP_TITLE, EXPERIENCE_EMPLOYMENT_TYPE, EXPERIENCE_START_DATE,
                               EXPERIENCE_END_DATE, EXP_COMPANY_NAME}:
                result.append(data)
        except Exception as e:
            print(e.args)
    return result if len(result) > 0 else None
