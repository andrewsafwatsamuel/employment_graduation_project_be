from domain.getaways.db_gateway.operations.company_db_operations import remove_company_phone
from domain.utils.validation_utils import is_valid_string_input


def remove_company_phone_use_case(company_id, phone, operation=remove_company_phone):
    if company_id is None:
        raise Exception("Invalid data")
    if not is_valid_string_input(phone):
        raise Exception("Invalid data")
    return operation(company_id, phone) > 0
