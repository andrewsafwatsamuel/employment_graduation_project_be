from entities.models.company import *
from entities.models.session import *
from domain.getaways.db_gateway.db_utils import *

insert_company_query = create_insert_query(COMPANY_TABLE_NAME, [
    COMPANY_LOGO,
    COMPANY_NAME,
    COMPANY_INDUSTRY,
    COMPANY_WEBSITE,
    COMPANY_ABOUT,
    COMPANY_EMAIL,
    COMPANY_FACEBOOK_PAGE,
    COMPANY_PASSWORD
])

insert_company_session_query = create_insert_query(COMPANY_SESSION_TABLE_NAME, [
    OWNER_ID, Auth_TOKEN, REFRESH_TOKEN, OWNER_EMAIL, CREATED_AT
])

retrieve_company_by_email_query = create_retrieve_query(
    table_name=COMPANY_TABLE_NAME,
    where_clause=[f"{COMPANY_EMAIL} ="]
)
