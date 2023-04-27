from entities.models.employee import *
from domain.getaways.db_gateway.db_utils import *

insert_employee_query = create_insert_query(EMPLOYEE_TABLE_NAME, [
    EMPLOYEE_photo, EMPLOYEE_BIO, EMPLOYEE_RESUME, EMPLOYEE_NAME, EMPLOYEE_PHONE, EMPLOYEE_EMAIL, EMPLOYEE_TITLE,
    EMPLOYEE_PASSWORD
])

retrieve_employee_by_email_query = create_retrieve_query(
    table_name=EMPLOYEE_TABLE_NAME,
    where_clause=[f"{EMPLOYEE_EMAIL} ="]
)
