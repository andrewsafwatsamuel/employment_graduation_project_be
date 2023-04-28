from entities.models.session import *
from domain.getaways.db_gateway.db_utils import *


def insert_new_session_query(table_name):
    return create_insert_query(table_name, [
        OWNER_ID, Auth_TOKEN, REFRESH_TOKEN, OWNER_EMAIL, CREATED_AT
    ])


def retrieve_session_by_token_query(table_name):
    return create_retrieve_query(
        table_name,
        where_clause=f"{Auth_TOKEN} = {parametrized_query(0)}"
    )


def delete_sessions_by_email_query(table_name):
    return create_delete_query(
        table_name,
        f"{OWNER_EMAIL} = {parametrized_query(0)}"
    )


def delete_session_by_token_query(table_name):
    return create_delete_query(
        table_name,
        f"{Auth_TOKEN} = {parametrized_query(0)}"
    )
