from domain.getaways.db_gateway.queries.employee_queries import *
from domain.getaways.db_gateway.db_manager import insert_new_record


def insert_employee(employee_db):
    return insert_new_record(insert_employee_query, (
        employee_db[EMPLOYEE_photo],
        employee_db[EMPLOYEE_BIO],
        employee_db[EMPLOYEE_RESUME],
        employee_db[EMPLOYEE_NAME],
        employee_db[EMPLOYEE_PHONE],
        employee_db[EMPLOYEE_EMAIL],
        employee_db[EMPLOYEE_TITLE],
        employee_db[EMPLOYEE_PASSWORD]
    ))


def insert_employee_session(session_db):
    return insert_new_record(insert_employee_session_query, (
        session_db[OWNER_ID],
        session_db[Auth_TOKEN],
        session_db[REFRESH_TOKEN],
        session_db[OWNER_EMAIL],
        session_db[CREATED_AT]
    ))
