from domain.getaways.db_gateway.operations.job_listing_db_operations import update_job_listing
from entities.models.job_listing import *
from domain.utils.job_listing_utils import is_valid_exp_level
from domain.utils.validation_utils import is_valid_string_input


def update_job_listing_use_case(job_listing_db, operation=update_job_listing):
    if job_listing_db[JOB_LISTING_ID] is None or job_listing_db[COMPANY_ID_FK] is None:
        raise Exception("Invalid data")
    if str(job_listing_db[JOB_LISTING_STATUS]) not in ['0', '1']:
        raise Exception("Invalid status")
    if not is_valid_exp_level(job_listing_db[JOB_LISTING_EXP_LEVEL]):
        raise Exception("Invalid experience level")
    if not is_valid_string_input(job_listing_db[JOB_LISTING_TITLE]):
        raise Exception("Invalid title")
    updated_rows = operation(job_listing_db)
    job_listing_db.pop(COMPANY_ID_FK)
    job_listing_db.pop(JOB_LISTING_ID)
    return job_listing_db if updated_rows > 0 else {"message": "No values updated"}
