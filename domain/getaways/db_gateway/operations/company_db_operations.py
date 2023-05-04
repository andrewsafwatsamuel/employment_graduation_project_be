from entities.models.company import *
from domain.getaways.db_gateway.db_utils import *
from domain.getaways.db_gateway.db_manager import *


def insert_company(company_db):
    insert_company_statement = create_insert_query(COMPANY_TABLE_NAME, [
        COMPANY_LOGO,
        COMPANY_NAME,
        COMPANY_INDUSTRY,
        COMPANY_WEBSITE,
        COMPANY_ABOUT,
        COMPANY_EMAIL,
        COMPANY_FACEBOOK_PAGE,
        COMPANY_PASSWORD
    ])
    return insert_new_record(insert_company_statement, (
        company_db[COMPANY_LOGO],
        company_db[COMPANY_NAME],
        company_db[COMPANY_INDUSTRY],
        company_db[COMPANY_WEBSITE],
        company_db[COMPANY_ABOUT],
        company_db[COMPANY_EMAIL],
        company_db[COMPANY_FACEBOOK_PAGE],
        company_db[COMPANY_PASSWORD]
    ))


def retrieve_company_by_email(email):
    retrieve_company_by_email_query = create_retrieve_query(
        table_name=COMPANY_TABLE_NAME,
        where_clause=f"{COMPANY_EMAIL} = {parametrized_query(0)}"
    )

    company_db = query_single_value(retrieve_company_by_email_query, [email])
    if company_db is None:
        return None
    else:
        return Company_Db(
            company_db[0],
            company_db[1],
            company_db[2],
            company_db[3],
            company_db[4],
            company_db[5],
            company_db[6],
            company_db[7],
            company_db[8]
        )
