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
        EMPLOYEE_PHOTO, EMPLOYEE_BIO, EMPLOYEE_RESUME, EMPLOYEE_NAME, EMPLOYEE_PHONE, EMPLOYEE_EMAIL, EMPLOYEE_TITLE,
        EMPLOYEE_PASSWORD
    ])
    values = (
        employee_db[EMPLOYEE_PHOTO], employee_db[EMPLOYEE_BIO], employee_db[EMPLOYEE_RESUME],
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


def retrieve_employee_with_experiences(emp_id):
    emp_db = __retrieve_employee_with_id(emp_id)
    if emp_db is not None:
        emp_db.update({EXPERIENCE_TABLE_NAME: __retrieve_experiences(emp_id)})
    return emp_db


def __retrieve_employee_with_id(emp_id):
    retrieve_employee_statement = create_retrieve_query(
        table_name=EMPLOYEE_TABLE_NAME,
        where_clause=f"{EMPLOYEE_ID} = {parametrized_query(0)}"
    )
    result = query_single_value(retrieve_employee_statement, [emp_id])
    if result is None:
        return None
    else:
        emp = Employee_Db(
            result[0],
            result[1],
            result[2],
            result[3],
            result[4],
            result[5],
            result[6],
            result[7],
            result[8]
        )
        emp.pop(EMPLOYEE_PASSWORD)
        return emp


def __retrieve_experiences(emp_id):
    retrieve_experiences_statement = create_retrieve_query(
        table_name=EXPERIENCE_TABLE_NAME,
        where_clause=f"{EMPLOYEE_ID_FK} = {parametrized_query(0)}"
    )
    rows = query_multiple_values(retrieve_experiences_statement, [emp_id])
    results = []
    for row in rows:
        result = Experience_Db(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6]
        )
        result.pop(EMPLOYEE_ID_FK)
        results.append(result)
    return results


def insert_experience(experience_db):
    query_statement = create_insert_query(
        EXPERIENCE_TABLE_NAME,
        [
            EMPLOYEE_ID_FK,
            EXP_COMPANY_NAME,
            EXPERIENCE_EMP_TITLE,
            EXPERIENCE_EMPLOYMENT_TYPE,
            EXPERIENCE_START_DATE,
            EXPERIENCE_END_DATE
        ])
    values = (experience_db[EMPLOYEE_ID_FK],
              experience_db[EXP_COMPANY_NAME],
              experience_db[EXPERIENCE_EMP_TITLE],
              experience_db[EXPERIENCE_EMPLOYMENT_TYPE],
              experience_db[EXPERIENCE_START_DATE],
              experience_db[EXPERIENCE_END_DATE])
    return insert_new_record(query_statement, values)


def update_emp_profile(emp_db):
    query_statement = f"""
        UPDATE {EMPLOYEE_TABLE_NAME} SET 
        {EMPLOYEE_BIO} = %s , 
        {EMPLOYEE_NAME} = %s , 
        {EMPLOYEE_PHONE} = %s , 
        {EMPLOYEE_EMAIL} = %s , 
        {EMPLOYEE_TITLE} = %s 
        WHERE {EMPLOYEE_ID} = %s;
    """
    values = (
        emp_db[EMPLOYEE_BIO],
        emp_db[EMPLOYEE_NAME],
        emp_db[EMPLOYEE_PHONE],
        emp_db[EMPLOYEE_EMAIL],
        emp_db[EMPLOYEE_TITLE],
        emp_db[EMPLOYEE_ID]
    )
    return update_db_entries(query_statement, values)


def update_emp_password(emp_id, password):
    query_statement = f""" UPDATE {EMPLOYEE_TABLE_NAME} SET {EMPLOYEE_PASSWORD} = %s WHERE {EMPLOYEE_ID} = %s;"""
    values = (password, emp_id)
    return update_db_entries(query_statement, values)


def remove_experience(emp_id, exp_id):
    query_statement = create_delete_query(
        EXPERIENCE_TABLE_NAME,
        f"{EMPLOYEE_ID_FK} = {{0}} AND {EXPERIENCE_ID} = {{1}}"
    )
    return delete_db_entries(query_statement, (emp_id, exp_id))
