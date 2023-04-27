from entities.models.session import *
from domain.getaways.db_gateway.db_utils import *


def insert_new_session_query(table_name):
    query = create_insert_query(table_name, [
        OWNER_ID, Auth_TOKEN, REFRESH_TOKEN, OWNER_EMAIL, CREATED_AT
    ])
    return query
