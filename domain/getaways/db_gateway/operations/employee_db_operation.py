from entities.models.employee import *
from domain.getaways.db_gateway.db_statement_utils import *
from domain.getaways.db_gateway.db_manager import *


def insert_employee(employee_db, experiences):
    return insert_on_many_tables(
        lambda db, cursor: insert_employee_with_experience_transaction(employee_db, experiences, db, cursor)
    )


def insert_employee_with_experience_transaction(employee_db, experiences, db, cursor):
    try:
        employee_id = __insert_to_employee_tabel(employee_db, cursor)
        if experiences is not None and len(experiences) > 0:
            __insert_into_experience_table(employee_id, experiences, cursor)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    return employee_id


def __insert_to_employee_tabel(employee_db, cursor):
    insert_employee_statement = create_insert_query(EMPLOYEE_TABLE_NAME, [
        EMPLOYEE_photo, EMPLOYEE_BIO, EMPLOYEE_RESUME, EMPLOYEE_NAME, EMPLOYEE_PHONE, EMPLOYEE_EMAIL, EMPLOYEE_TITLE,
        EMPLOYEE_PASSWORD
    ])
    values = (
        employee_db[EMPLOYEE_photo], employee_db[EMPLOYEE_BIO], employee_db[EMPLOYEE_RESUME],
        employee_db[EMPLOYEE_NAME], employee_db[EMPLOYEE_PHONE], employee_db[EMPLOYEE_EMAIL],
        employee_db[EMPLOYEE_TITLE], employee_db[EMPLOYEE_PASSWORD]
    )
    cursor.execute(insert_employee_statement, values)
    return cursor.lastrowid


def __insert_into_experience_table(emp_id, experiences, cursor):
    insert_experiences_statement = create_insert_multi_values_query(EXPERIENCE_TABLE_NAME, (
        EMPLOYEE_ID_FK,
        EXP_COMPANY_NAME,
        EXPERIENCE_EMP_TITLE,
        EXPERIENCE_EMPLOYMENT_TYPE,
        EXPERIENCE_START_DATE,
        EXPERIENCE_END_DATE
    ), len(experiences))
    values = __flatten_experiences_values(emp_id, experiences)
    cursor.execute(insert_experiences_statement, values)


def __flatten_experiences_values(foreign_key, dict_array):
    result = []
    for dictionary in dict_array:
        result.append(foreign_key)
        result.append(dictionary[EXP_COMPANY_NAME])
        result.append(dictionary[EXPERIENCE_EMP_TITLE])
        result.append(dictionary[EXPERIENCE_EMPLOYMENT_TYPE])
        result.append(dictionary[EXPERIENCE_START_DATE])
        result.append(dictionary[EXPERIENCE_END_DATE])
    return result


def retrieve_employee_by_email(email):
    retrieve_employee_by_email_query = create_retrieve_query(
        table_name=EMPLOYEE_TABLE_NAME,
        where_clause=f"{EMPLOYEE_EMAIL} = {parametrized_query(0)}"
    )
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
