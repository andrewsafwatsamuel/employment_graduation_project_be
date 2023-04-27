from domain.getaways.db_gateway.queries.company_queries import *
from domain.getaways.db_gateway.db_manager import *


def insert_company(company_db):
    return insert_new_record(insert_company_query, (
        company_db[COMPANY_LOGO],
        company_db[COMPANY_NAME],
        company_db[COMPANY_INDUSTRY],
        company_db[COMPANY_WEBSITE],
        company_db[COMPANY_ABOUT],
        company_db[COMPANY_EMAIL],
        company_db[COMPANY_FACEBOOK_PAGE],
        company_db[COMPANY_PASSWORD]
    ))


def insert_company_session(session_db):
    return insert_new_record(insert_company_session_query, (
        session_db[OWNER_ID],
        session_db[Auth_TOKEN],
        session_db[REFRESH_TOKEN],
        session_db[OWNER_EMAIL],
        session_db[CREATED_AT]
    ))


def retrieve_company_by_email(email):
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
