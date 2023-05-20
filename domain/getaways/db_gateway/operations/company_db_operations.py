from domain.getaways.db_gateway.db_manager import *
from domain.getaways.db_gateway.db_statement_utils import *
from entities.models.company import *


def insert_company(company_db, company_phones):
    return insert_on_many_tables(
        lambda db, cursor: company_insertion_operations(company_db, company_phones, db, cursor))


def company_insertion_operations(company_db, company_phones, db, cursor):
    insert_company_statement = create_insert_query(COMPANY_TABLE_NAME, [
        COMPANY_LOGO,
        COMPANY_NAME,
        COMPANY_INDUSTRY,
        COMPANY_WEBSITE,
        COMPANY_ABOUT,
        COMPANY_EMAIL,
        COMPANY_FACEBOOK_PAGE,
        COMPANY_PASSWORD
    ])
    insert_company_phones_statement = create_insert_multi_values_query(
        COMPANY_PHONE_TABLE_NAME, [
            COMPANY_ID_FK,
            COMPANY_PHONE
        ], len(company_phones)
    )
    try:
        cursor.execute(insert_company_statement, (
            company_db[COMPANY_LOGO],
            company_db[COMPANY_NAME],
            company_db[COMPANY_INDUSTRY],
            company_db[COMPANY_WEBSITE],
            company_db[COMPANY_ABOUT],
            company_db[COMPANY_EMAIL],
            company_db[COMPANY_FACEBOOK_PAGE],
            company_db[COMPANY_PASSWORD]
        ))
        company_id = cursor.lastrowid
        values = []
        for phone in company_phones:
            values.append(company_id)
            values.append(phone)
        cursor.execute(insert_company_phones_statement, values)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    return company_id


def retrieve_company_by_email(email):
    retrieve_company_by_email_query = create_retrieve_query(
        table_name=COMPANY_TABLE_NAME,
        where_clause=f"{COMPANY_EMAIL} = {parametrized_query(0)}"
    )

    company_db = query_single_value(retrieve_company_by_email_query, [email])
    if company_db is None:
        return None
    else:
        return Company_Db(
            company_db[0],
            company_db[1],
            company_db[2],
            company_db[3],
            company_db[4],
            company_db[5],
            company_db[6],
            company_db[7],
            company_db[8]
        )


def retrieve_company_by_id(company_id):
    company = __retrieve_company_by_id(company_id)
    if company is not None:
        company.update({COMPANY_PHONE_TABLE_NAME: __retrieve_company_phones(company_id)})
    return company


def __retrieve_company_by_id(company_id):
    retrieve_company_by_id_statement = create_retrieve_query(
        table_name=COMPANY_TABLE_NAME,
        where_clause=f"{COMPANY_ID} = {parametrized_query(0)}"
    )
    result = query_single_value(retrieve_company_by_id_statement, [company_id])
    if result is None:
        return None
    else:
        company = Company_Db(
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
        company.pop(COMPANY_PASSWORD)
        return company


def __retrieve_company_phones(company_id):
    retrieve_company_phones = create_retrieve_query(
        COMPANY_PHONE_TABLE_NAME,
        [COMPANY_PHONE],
        f"{COMPANY_ID_FK} = {parametrized_query(0)}"
    )
    rows = query_multiple_values(retrieve_company_phones, [company_id])
    results = []
    for row in rows:
        results.append(row[0])
    return results


def add_new_phone(company_id, phone):
    query_statement = create_insert_query(COMPANY_PHONE_TABLE_NAME, [COMPANY_ID_FK, COMPANY_PHONE])
    return insert_new_record(query_statement, (company_id, phone))


def update_company_profile(company_db):
    query_statement = f"""
         UPDATE {COMPANY_TABLE_NAME} SET 
         {COMPANY_NAME} = %s , 
         {COMPANY_INDUSTRY} = %s , 
         {COMPANY_WEBSITE} = %s , 
         {COMPANY_ABOUT} = %s , 
         {COMPANY_EMAIL} = %s , 
         {COMPANY_FACEBOOK_PAGE} = %s 
         WHERE {COMPANY_ID} = %s;
    """
    values = (
        company_db[COMPANY_NAME],
        company_db[COMPANY_INDUSTRY],
        company_db[COMPANY_WEBSITE],
        company_db[COMPANY_ABOUT],
        company_db[COMPANY_EMAIL],
        company_db[COMPANY_FACEBOOK_PAGE],
        company_db[COMPANY_ID]
    )
    return update_db_entries(query_statement, values)


def update_company_password(company_id, password):
    query_statement = f""" UPDATE {COMPANY_TABLE_NAME} SET {COMPANY_PASSWORD} = %s WHERE {COMPANY_ID} = %s;"""
    values = (password, company_id)
    return update_db_entries(query_statement, values)


def remove_company_phone(company_id, phone):
    query_statement = create_delete_query(
        COMPANY_PHONE_TABLE_NAME,
        f"{COMPANY_ID_FK} = {{0}} AND {COMPANY_PHONE} = {{1}}"
    )
    return delete_db_entries(query_statement, (company_id, phone))
