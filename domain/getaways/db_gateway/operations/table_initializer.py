from domain.getaways.db_gateway.queries.table_creation_queries import *
from domain.getaways.db_gateway.db_manager import *


def init_db_tables():
    make_db_query(employee_creation_query)
    make_db_query(company_creationQuery)
    make_db_query(company_phone_creation_query)
    make_db_query(company_address_creation_query)
    make_db_query(job_listing_creation_query)
    make_db_query(job_application_creation_query)
    make_db_query(experience_creation_query)
    make_db_query(company_session_creation_query)
    make_db_query(employee_session_creation_query)
