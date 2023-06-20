from domain.getaways.db_gateway.db_statement_utils import *
from domain.getaways.db_gateway.db_manager import *
from entities.models.session import *


def insert_session(session_db, table_name):
    insert_session_query = create_insert_query(table_name, [
        OWNER_ID, Auth_TOKEN, REFRESH_TOKEN, OWNER_EMAIL, CREATED_AT
    ])
    row = insert_new_record(insert_session_query, (
        session_db[OWNER_ID],
        session_db[Auth_TOKEN],
        session_db[REFRESH_TOKEN],
        session_db[OWNER_EMAIL],
        session_db[CREATED_AT]
    ))
    return row


def retrieve_session_by_token(auth_token, table_name):
    query = create_retrieve_query(
        table_name,
        where_clause=f"{Auth_TOKEN} = {parametrized_query(0)}"
    )
    session = query_single_value(query, [auth_token])
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


def delete_sessions_by_id(owner_id, table_name):
    delete_session_statement = create_delete_query(
        table_name,
        f"{OWNER_ID} = {parametrized_query(0)}"
    )
    return delete_db_entries(delete_session_statement, [owner_id])


def delete_session_by_token(auth_token, table_name):
    delete_session_statement = create_delete_query(
        table_name,
        f"{Auth_TOKEN} = {parametrized_query(0)}"
    )
    return delete_db_entries(delete_session_statement, [auth_token])
