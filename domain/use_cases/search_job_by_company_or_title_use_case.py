from domain.utils.validation_utils import is_valid_string_input
from domain.getaways.db_gateway.operations.job_listing_db_operations import search_job_listing_by_company_or_title


def search_job_by_company_or_title_use_case(search_key, operation=search_job_listing_by_company_or_title):
    if not is_valid_string_input(search_key):
        raise Exception("Search keyword is not valid")
    return operation(search_key)
