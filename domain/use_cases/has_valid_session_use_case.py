from domain.getaways.db_gateway.operations.session_db_operations import *
from domain.utils.validation_utils import is_valid_string_input
from domain.utils.time_utils import current_time_millis

one_week_millis = 604800000


def has_valid_session_use_case(
        auth_token,
        table_name,
        expiry_duration=one_week_millis,
        operation=retrieve_session_by_token
):
    if not is_valid_string_input(auth_token):
        return False
    session = operation(auth_token, table_name)
    return False if session is None or (current_time_millis() - session[CREATED_AT]) > expiry_duration else True
