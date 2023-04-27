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
