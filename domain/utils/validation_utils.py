from domain.utils.time_utils import current_time_millis
from entities.models.session import CREATED_AT
import re

one_week_millis = 604800000


def has_valid_session(session, expiry_duration=one_week_millis):
    return session is not None and (current_time_millis() - session[CREATED_AT]) < expiry_duration


def is_valid_string_input(input, pattern=None):
    return (input is not None) \
        and (len(input.strip()) > 0) \
        and (re.match(pattern if pattern is not None else ".*", input))
