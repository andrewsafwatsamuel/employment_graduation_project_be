from domain.utils.validation_utils import has_valid_session
from domain.utils.dict_utils import get_or_none
from entities.constants.constants import AUTH_TOKEN
from domain.use_cases.get_session_by_token_use_case import *


def get_user_session(request_headers, table, session_use_case=get_session_by_token_use_case):
    auth_token = get_or_none(request_headers, AUTH_TOKEN)
    if auth_token is None:
        return {"message": "unauthorized"}
    try:
        session = session_use_case(auth_token, table)
    except Exception as e:
        return {"message": str(e.args)}
    if not has_valid_session(session):
        return {"message": "unauthorized"}
    return session
