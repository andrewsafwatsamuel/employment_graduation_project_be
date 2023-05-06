from domain.getaways.db_gateway.operations.session_db_operations import *
from domain.utils.validation_utils import is_valid_string_input


def get_session_by_token_use_case(auth_token, table_name, operation=retrieve_session_by_token):
    if not is_valid_string_input(auth_token):
        raise Exception("Unauthorized")
    return operation(auth_token, table_name)
