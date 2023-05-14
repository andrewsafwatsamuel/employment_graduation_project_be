from domain.utils.validation_utils import is_valid_string_input
from entities.models.job_listing import *


def is_valid_exp_level(exp_level):
    return is_valid_string_input(exp_level) and exp_level.lower().strip() in (INTERN, JUNIOR, MID_LEVEL, SENIOR, LEAD)
