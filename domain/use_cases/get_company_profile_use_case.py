from domain.getaways.db_gateway.operations.company_db_operations import retrieve_company_by_id


def get_company_profile_use_case(company_id, operation=retrieve_company_by_id):
    if company_id is None:
        raise Exception("Something went wrong")
    return operation(company_id)
