from domain.getaways.db_gateway.operations.job_listing_db_operations import *
from domain.utils.validation_utils import *
from domain.utils.job_listing_utils import is_valid_exp_level


def add_new_job_listing_use_case(job_listing_db, operation=insert_new_job_listing):
    if job_listing_db[COMPANY_ID_FK] is None:
        raise Exception("Invalid company id")
    if not is_valid_exp_level(job_listing_db[JOB_LISTING_EXP_LEVEL]):
        raise Exception("Invalid experience level")
    if not is_valid_string_input(job_listing_db[JOB_LISTING_TITLE]):
        raise Exception("Job title is mandatory")
    if job_listing_db[JOB_LISTING_STATUS] is None:
        job_listing_db.update({JOB_LISTING_STATUS: 1})
    return operation(job_listing_db)
