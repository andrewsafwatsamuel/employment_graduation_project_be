from domain.getaways.db_gateway.operations.job_listing_db_operations import retrieve_job_applications


def get_job_applications_use_case(company_id, job_listing_id, operation=retrieve_job_applications):
    if company_id is None or job_listing_id is None:
        raise Exception("Something went wrong")
    return operation(company_id, job_listing_id)
