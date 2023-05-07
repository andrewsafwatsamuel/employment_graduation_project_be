from entities.models.job_listing import *
from domain.getaways.db_gateway.operations.job_listing_db_operations import insert_new_job_application


def apply_for_job_use_case(job_application_db, operation=insert_new_job_application):
    if job_application_db[EMPLOYEE_ID_FK] is None or job_application_db[JOB_LISTING_ID_FK] is None:
        raise Exception("Invalid inputs")
    job_application_db.update({JOB_APPLICATION_STATUS: APPLICATION_OPEN})
    inserted_successfully = operation(job_application_db) is not None
    return inserted_successfully
