from entities.models.company import *
from domain.getaways.db_gateway.operations.company_db_operations import retrieve_company_by_email, \
    update_company_password
from entities.constants.regex import *
from werkzeug.security import check_password_hash, generate_password_hash
from domain.utils.validation_utils import is_valid_string_input


def update_company_password_use_case(
        email,
        old_password,
        new_password,
        retrieve_company_operation=retrieve_company_by_email,
        update_password_operation=update_company_password
):
    if not is_valid_string_input(email, EMAIL_ADDRESS_REGEX) or not is_valid_string_input(old_password):
        raise Exception("Invalid inputs")
    if not is_valid_string_input(new_password, PASSWORD_REGEX):
        raise Exception("Invalid new password")
    company = retrieve_company_operation(email)
    if company is None or not check_password_hash(company[COMPANY_PASSWORD], old_password):
        raise Exception("Invalid inputs")
    encrypted_password = generate_password_hash(new_password)
    return update_password_operation(company[COMPANY_ID], encrypted_password) > 0
