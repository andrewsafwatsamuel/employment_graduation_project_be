from domain.getaways.db_gateway.operations.employee_db_operation import insert_employee_session
from domain.getaways.db_gateway.operations.company_db_operations import insert_company_session
from werkzeug.security import generate_password_hash
from entities.models.session import *
from domain.utils.validation_utils import is_valid_string_input
from entities.constants.regex import EMAIL_ADDRESS_REGEX
import time

SESSION_TYPE_EMP = "employee_session"
SESSION_TYPE_COMPANY = "company_session"


def create_session_use_case(
        owner_id,
        owner_email,
        session_type,
        employee_operation=insert_employee_session,
        session_operation=insert_company_session
):
    if not is_valid_string_input(str(owner_id)) or not is_valid_string_input(owner_email, EMAIL_ADDRESS_REGEX):
        raise Exception("Error while creating the session")
    token_combination = f"{owner_id}-{owner_email}"
    auth_token = generate_password_hash(token_combination)
    refresh_token = generate_password_hash(token_combination)
    current_time = int(round(time.time()) * 1000)
    session_db = Session_Db(owner_id, auth_token, refresh_token, owner_email, current_time)
    # TODO retrieve and delete sessions with the same email
    session_row_id = None
    if session_type == SESSION_TYPE_EMP:
        session_row_id = employee_operation(session_db)
    elif session_type == SESSION_TYPE_COMPANY:
        session_row_id = session_operation(session_db)
    if session_row_id is not None:
        return session_db
    else:
        raise Exception("Error while creating the session")
