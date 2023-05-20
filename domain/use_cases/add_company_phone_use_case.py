from domain.getaways.db_gateway.operations.company_db_operations import add_new_phone
from domain.utils.validation_utils import is_valid_string_input
from entities.constants.regex import EGYPTIAL_PHONE_NUMBER_REGEX


def add_company_phone_use_case(company_id, company_phone, operation=add_new_phone):
    if company_id is None:
        raise Exception("Invalid data")
    if not is_valid_string_input(company_phone, EGYPTIAL_PHONE_NUMBER_REGEX):
        raise Exception("Invalid phone number")
    return operation(company_id, company_phone) is not None
