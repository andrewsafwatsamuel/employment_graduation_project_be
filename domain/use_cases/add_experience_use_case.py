from domain.getaways.db_gateway.operations.employee_db_operation import insert_experience
from domain.utils.validation_utils import is_valid_string_input
from entities.models.employee import *


def add_experience_use_case(experience_db, operation: insert_experience):
    if experience_db[EMPLOYEE_ID_FK] is None:
        raise Exception("Invalid data")
    if not is_valid_string_input(experience_db[EXP_COMPANY_NAME]):
        raise Exception("Company name must not be null or blank")
    if not is_valid_string_input(experience_db[EXPERIENCE_EMP_TITLE]):
        raise Exception("Title must not be null or blank")
    if not __is_valid_employment_type(experience_db[EMPLOYEE_ID_FK]):
        raise Exception("Invalid employment type")
    if not is_valid_string_input(experience_db[EXPERIENCE_START_DATE]):
        raise Exception("Start date must not be null or blank")
    return operation(experience_db) is not None


def __is_valid_employment_type(employment_type):
    return employment_type is not None and str(employment_type) in [str(FULL_TIME), str(PART_TIME), str(CONTRACTOR)]
