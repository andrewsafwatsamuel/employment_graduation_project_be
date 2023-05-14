from domain.getaways.db_gateway.operations.job_listing_db_operations import *
from domain.utils.validation_utils import is_valid_string_input

__application_statuses = [APPLICATION_OPEN, APPLICATION_INTERVIEWING, APPLICATION_ACCEPTED, APPLICATION_REJECTED]


def update_application_status_use_case(
        job_application_db,
        company_id,
        new_status,
        retrieve_job=retrieve_job_by_id,
        update_operation=update_job_application_status
):
    if not __has_valid_ids(job_application_db[JOB_LISTING_ID_FK], job_application_db[EMPLOYEE_ID_FK], company_id):
        raise Exception("Invalid id")
    if not is_valid_string_input(new_status) or new_status not in __application_statuses:
        raise Exception("Invalid application status")
    job_listing = retrieve_job(job_application_db[JOB_LISTING_ID_FK])
    if job_listing is None:
        raise Exception("Invalid data")
    elif job_listing[COMPANY_ID_FK] != company_id:
        raise Exception("unauthorized")
    update_operation(new_status, job_application_db[JOB_LISTING_ID_FK], job_application_db[EMPLOYEE_ID_FK])


def __has_valid_ids(job_listing_id, emp_id, comp_id):
    return job_listing_id is not None and emp_id is not None and comp_id is not None
