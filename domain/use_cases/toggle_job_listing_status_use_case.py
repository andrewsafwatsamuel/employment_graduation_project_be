from domain.getaways.db_gateway.operations.job_listing_db_operations import update_job_listing_status, \
    retrieve_job_by_id
from entities.models.job_listing import *


def toggle_job_listing_status_use_case(
        job_listing_id,
        company_id,
        update_operation=update_job_listing_status,
        retrieve_operation=retrieve_job_by_id
):
    if job_listing_id is None:
        raise Exception("Invalid id")
    job_listing = retrieve_operation(job_listing_id)
    if job_listing is None:
        raise Exception("Invalid data")
    elif job_listing[COMPANY_ID_FK] != company_id:
        raise Exception("unauthorized")
    status = 0 if job_listing[JOB_LISTING_STATUS] == 1 else 1
    update_operation(job_listing_id, status)
    return status
