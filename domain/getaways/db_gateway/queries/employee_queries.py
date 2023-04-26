from entities.models.employee import *
from entities.models.session import *
from domain.getaways.db_gateway.db_utils import create_insert_query

insert_employee_query = create_insert_query(EMPLOYEE_TABLE_NAME, [
    EMPLOYEE_photo, EMPLOYEE_BIO, EMPLOYEE_RESUME, EMPLOYEE_NAME, EMPLOYEE_PHONE, EMPLOYEE_EMAIL, EMPLOYEE_TITLE,
    EMPLOYEE_PASSWORD
])

insert_employee_session_query = create_insert_query(EMPLOYEE_SESSION_TABLE_NAME, [
    OWNER_ID, Auth_TOKEN, REFRESH_TOKEN, OWNER_EMAIL, CREATED_AT
])
