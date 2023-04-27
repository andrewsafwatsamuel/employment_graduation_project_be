from entities.models.company import *
from domain.getaways.db_gateway.operations.company_db_operations import retrieve_company_by_email
from entities.constants.regex import *
from werkzeug.security import check_password_hash
from domain.utils.validation_utils import is_valid_string_input


def invalid_login_credentials():
    return Exception("Invalid email, or password")


def company_login_use_case(email, password, operation=retrieve_company_by_email):
    if not is_valid_string_input(email, EMAIL_ADDRESS_REGEX) or not is_valid_string_input(password, PASSWORD_REGEX):
        raise invalid_login_credentials()
    company = operation(email)
    if company is None or not check_password_hash(company[COMPANY_PASSWORD], password):
        raise invalid_login_credentials()
    return company
