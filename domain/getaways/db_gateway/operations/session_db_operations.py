from domain.getaways.db_gateway.queries.session_queries import *
from domain.getaways.db_gateway.db_manager import *
from entities.models.session import *


def insert_session(session_db, table_name):
    row = insert_new_record(insert_new_session_query(table_name), (
        session_db[OWNER_ID],
        session_db[Auth_TOKEN],
        session_db[REFRESH_TOKEN],
        session_db[OWNER_EMAIL],
        session_db[CREATED_AT]
    ))
    return row


def retrieve_session_by_token(auth_token, table_name):
    session = query_single_value(retrieve_session_by_token_query(table_name), [auth_token])
    if session is None:
        return None
    else:
        return Session_Db(
            session[0],
            session[1],
            session[2],
            session[3],
            session[4]
        )


def delete_sessions_by_email(email, table_name):
    return delete_db_entries(delete_sessions_by_email_query(table_name), [email])


def delete_session_by_token(auth_token, table_name):
    return delete_db_entries(delete_session_by_token_query(table_name), [auth_token])
