from domain.getaways.db_gateway.db_manager import *
from domain.getaways.db_gateway.db_statement_utils import *
from entities.models.job_listing import *
from entities.models.company import *


def insert_new_job_listing(job_listing_db):
    insert_job_listing_statement = create_insert_query(JOB_LISTING_TABLE_NAME, [
        COMPANY_ID_FK, JOB_LISTING_EXP_LEVEL, JOB_LISTING_TITLE, JOB_LISTING_STATUS, JOB_LISTING_DESCRIPTION
    ])
    return insert_new_record(insert_job_listing_statement, (
        job_listing_db[COMPANY_ID_FK],
        job_listing_db[JOB_LISTING_EXP_LEVEL],
        job_listing_db[JOB_LISTING_TITLE],
        job_listing_db[JOB_LISTING_STATUS],
        job_listing_db[JOB_LISTING_DESCRIPTION]
    ))


def search_job_listing_by_company_or_title(search_key):
    company_name = get_column(COMPANY_TABLE_NAME, COMPANY_NAME)
    job_listing_title = get_column(JOB_LISTING_TABLE_NAME, JOB_LISTING_TITLE)
    retrieve_job_listing_query = f"""
       SELECT {company_name} ,
              {job_listing_title} , 
              {get_column(JOB_LISTING_TABLE_NAME, JOB_LISTING_DESCRIPTION)} , 
              {get_column(JOB_LISTING_TABLE_NAME, JOB_LISTING_EXP_LEVEL)} , 
              {get_column(JOB_LISTING_TABLE_NAME, JOB_LISTING_ID)}
       FROM   {JOB_LISTING_TABLE_NAME}, {COMPANY_TABLE_NAME} 
       WHERE {get_column(JOB_LISTING_TABLE_NAME, COMPANY_ID_FK)}  = {get_column(COMPANY_TABLE_NAME, COMPANY_ID)}  
       AND   {get_column(JOB_LISTING_TABLE_NAME, JOB_LISTING_STATUS)} = {JOB_OPEN} 
       AND ( {company_name} LIKE '%{{0}}%' OR {job_listing_title} LIKE '%{{0}}%');   
    """
    raw_values = query_multiple_values(retrieve_job_listing_query, [search_key])
    results = []
    for value in raw_values:
        results.append({
            COMPANY_TABLE_NAME: value[0],
            JOB_LISTING_TITLE: value[1],
            JOB_LISTING_DESCRIPTION: value[2],
            JOB_LISTING_EXP_LEVEL: value[3],
            JOB_LISTING_ID: value[4]
        })
    return results if len(results) > 0 else None


def insert_new_job_application(job_application_db):
    query = create_insert_query(JOB_APPLICATION_TABLE_NAME, [EMPLOYEE_ID_FK, JOB_LISTING_ID_FK, JOB_APPLICATION_STATUS])
    values = (job_application_db[EMPLOYEE_ID_FK], job_application_db[JOB_LISTING_ID_FK],
              job_application_db[JOB_APPLICATION_STATUS])
    return insert_new_record(query, values)
