from entities.models.company import COMPANY_ID_FK

# employee variable names
EMPLOYEE_TABLE_NAME = "employee"
EMPLOYEE_ID = "id"
EMPLOYEE_PHOTO = "photo"
EMPLOYEE_BIO = "bio"
EMPLOYEE_RESUME = "resume"
EMPLOYEE_NAME = "name"
EMPLOYEE_PHONE = "phone"
EMPLOYEE_EMAIL = "email"
EMPLOYEE_TITLE = "title"
EMPLOYEE_PASSWORD = "password"
EMPLOYEE_ID_FK = "emp_id"

# experience variable names
EXPERIENCE_TABLE_NAME = "experience"
EXPERIENCE_EMP_TITLE = "title"
EXPERIENCE_EMPLOYMENT_TYPE = "employment_type"
EXPERIENCE_START_DATE = "start_date"
EXPERIENCE_END_DATE = "end_date"
EXP_COMPANY_NAME = "company_name"

# experience employment types
FULL_TIME = 0
PART_TIME = 1
CONTRACTOR = 2


# database model
def Employee_Db(
        emp_id,  # int not null
        photo,  # string nullable
        bio,  # string nullable
        resume,  # string nullable
        name,  # string not null
        phone,  # string not null
        email,  # string not null
        title,  # string nullable
        password,  # string not null
        experiences=None  # array of employee experiences
):
    return {
        EMPLOYEE_ID: emp_id,
        EMPLOYEE_PHOTO: photo,
        EMPLOYEE_BIO: bio,
        EMPLOYEE_RESUME: resume,
        EMPLOYEE_NAME: name,
        EMPLOYEE_PHONE: phone,
        EMPLOYEE_EMAIL: email,
        EMPLOYEE_TITLE: title,
        EMPLOYEE_PASSWORD: password,
        EXPERIENCE_TABLE_NAME: experiences
    }


def Experience_Db(
        emp_id,
        company_name,
        emp_title,
        employment_type,
        start_date,
        end_date
):
    return {
        EMPLOYEE_ID_FK: emp_id,
        EXP_COMPANY_NAME: company_name,
        EXPERIENCE_EMP_TITLE: emp_title,
        EXPERIENCE_EMPLOYMENT_TYPE: employment_type,
        EXPERIENCE_START_DATE: start_date,
        EXPERIENCE_END_DATE: end_date
    }
