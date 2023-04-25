from domain.getaways.db_gateway.table_creation_queries import  *
from domain.getaways.db_gateway.database import *


def init_db_tables():
    make_db_query(empoyee_creation_query)
    make_db_query(company_creationQuery)
    make_db_query(company_phone_creation_query)
    make_db_query(company_address_creation_query)
    make_db_query(job_listing_creation_query)
    make_db_query(job_application_creation_query)

