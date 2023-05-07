from domain.getaways.db_gateway.operations.job_listing_db_operations import retrieve_jobs_by_company_id


def get_all_jobs_by_company_id_use_case(company_id, operation=retrieve_jobs_by_company_id):
    if company_id is None:
        raise Exception("Invalid company id")
    return operation(company_id)
