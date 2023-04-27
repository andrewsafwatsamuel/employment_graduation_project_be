from entities.models.company import *
from domain.getaways.db_gateway.operations.company_db_operations import insert_company
from entities.constants.regex import *
from werkzeug.security import generate_password_hash
from domain.utils.validation_utils import is_valid_string_input


def company_registration_use_case(company_db, operation=insert_company):
    if not is_valid_string_input(company_db[COMPANY_PASSWORD], PASSWORD_REGEX):
        raise Exception("Invalid password")
    if not is_valid_string_input(company_db[COMPANY_EMAIL], EMAIL_ADDRESS_REGEX):
        raise Exception("Invalid email address")
    if not is_valid_string_input(company_db[COMPANY_NAME]):
        raise Exception("Name field is mandatory")
    if not is_valid_string_input(company_db[COMPANY_INDUSTRY]):
        raise Exception("Industry field is mandatory")
    if not is_valid_string_input(company_db[COMPANY_FACEBOOK_PAGE]):
        raise Exception("Facebook page field is mandatory")
    hashed_password = generate_password_hash(company_db[COMPANY_PASSWORD])
    company_db.update({COMPANY_PASSWORD: hashed_password})
    return operation(company_db)
