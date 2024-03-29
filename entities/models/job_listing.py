from entities.models.company import COMPANY_ID_FK
from entities.models.employee import EMPLOYEE_ID_FK, EMPLOYEE_NAME, EMPLOYEE_TITLE, EMPLOYEE_PHOTO

# Job listing variable names
JOB_LISTING_TABLE_NAME = "job_listing"
JOB_LISTING_ID = "id"
JOB_LISTING_EXP_LEVEL = "exp_level"
JOB_LISTING_TITLE = "title"
JOB_LISTING_STATUS = "status"
JOB_LISTING_DESCRIPTION = "description"
JOB_LISTING_ID_FK = "job_listing_id"

# application
JOB_APPLICATION_TABLE_NAME = "job_application"
JOB_APPLICATION_STATUS = "status"

# Job listing status
JOB_CLOSED = 0
JOB_OPEN = 1

# exp level
INTERN = "intern"
JUNIOR = "junior"
MID_LEVEL = "mid level"
SENIOR = "senior"
LEAD = "lead"

# Application status
APPLICATION_OPEN = "open"
APPLICATION_INTERVIEWING = "interviewing"
APPLICATION_ACCEPTED = "accepted"
APPLICATION_REJECTED = "rejected"


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
        JOB_LISTING_DESCRIPTION: description
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


def Job_Application_Api(
        emp_name,
        emp_id,
        emp_title,
        emp_photo,
        status
):
    return {
        EMPLOYEE_NAME: emp_name,
        EMPLOYEE_ID_FK: emp_id,
        EMPLOYEE_TITLE: emp_title,
        EMPLOYEE_PHOTO: emp_photo,
        JOB_APPLICATION_STATUS: status
    }
