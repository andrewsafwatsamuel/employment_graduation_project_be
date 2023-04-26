from entities.models.company import COMPANY_ID_FK
from entities.models.employee import EMPLOYEE_ID_FK

# Job listing variable names
JOB_LISTING_ID = "id"
JOB_LISTING_EXP_LEVEL = "exp_level"
JOB_LISTING_TITLE = "title"
JOB_LISTING_STATUS = "status"
JOB_LISTING_DISCRIPTION = "description"
JOB_LISTING_ID_FK = "job_listing_id"
JOB_APPLICATION_STATUS = "status"


def Job_Listing_Db(
        job_listing_id,
        company_id,
        exp_level,
        title,
        status,
        description
):
    return {
        JOB_LISTING_ID: job_listing_id,
        COMPANY_ID_FK: company_id,
        JOB_LISTING_EXP_LEVEL: exp_level,
        JOB_LISTING_TITLE: title,
        JOB_LISTING_STATUS: status,
        JOB_LISTING_DISCRIPTION: description
    }


def Job_Application_Db(
        emp_id,
        job_listing_id,
        status
):
    return {
        EMPLOYEE_ID_FK: emp_id,
        JOB_LISTING_ID_FK: job_listing_id,
        JOB_APPLICATION_STATUS: status
    }
