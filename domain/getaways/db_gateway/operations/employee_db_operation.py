from domain.getaways.db_gateway.queries.employee_queries import *
from domain.getaways.db_gateway.db_manager import *


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


def retrieve_employee_by_email(email):
    emp_db = query_single_value(retrieve_employee_by_email_query, [email])
    if emp_db is None:
        return None
    else:
        return Employee_Db(
            emp_db[0],
            emp_db[1],
            emp_db[2],
            emp_db[3],
            emp_db[4],
            emp_db[5],
            emp_db[6],
            emp_db[7],
            emp_db[8]
        )
