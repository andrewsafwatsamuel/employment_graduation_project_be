from domain.getaways.db_gateway.operations.company_db_operations import update_company_profile
from domain.utils.validation_utils import is_valid_string_input
from entities.constants.regex import *
from entities.models.company import *


def update_company_profile_use_case(company_db, operation=update_company_profile):
    if company_db[COMPANY_ID] is None:
        raise Exception("Invalid data")
    if not is_valid_string_input(company_db[COMPANY_NAME]):
        raise Exception("Company name must not be null or blank")
    if not is_valid_string_input(company_db[COMPANY_INDUSTRY]):
        raise Exception("Industry must not be null or blank")
    if not is_valid_string_input(company_db[COMPANY_EMAIL], EMAIL_ADDRESS_REGEX):
        raise Exception("Invalid Email")
    if not is_valid_string_input(company_db[COMPANY_FACEBOOK_PAGE]):
        raise Exception("Facebook page must not be null or blank")
    return operation(company_db) > 0
