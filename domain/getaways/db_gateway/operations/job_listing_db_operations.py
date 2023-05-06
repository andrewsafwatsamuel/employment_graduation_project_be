from domain.getaways.db_gateway.db_manager import *
from domain.getaways.db_gateway.db_statement_utils import *
from entities.models.job_listing import *


def insert_new_job_listing(company_id, job_listing_db):
    insert_job_listing_statement = create_insert_query(JOB_LISTING_TABLE_NAME, [
        COMPANY_ID_FK, JOB_LISTING_EXP_LEVEL, JOB_LISTING_TITLE, JOB_LISTING_STATUS, JOB_LISTING_DESCRIPTION
    ])
    return insert_new_record(insert_job_listing_statement, (
        company_id,
        job_listing_db[JOB_LISTING_EXP_LEVEL],
        job_listing_db[JOB_LISTING_TITLE],
        job_listing_db[JOB_LISTING_STATUS],
        job_listing_db[JOB_LISTING_DESCRIPTION]
    ))
