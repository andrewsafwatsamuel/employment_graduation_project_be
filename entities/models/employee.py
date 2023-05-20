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
EXPERIENCE_ID = "id"
EXPERIENCE_EMP_TITLE = "title"
EXPERIENCE_EMPLOYMENT_TYPE = "employment_type"
EXPERIENCE_START_DATE = "start_date"
EXPERIENCE_END_DATE = "end_date"
EXPERIENCE_COMPANY_NAME = "company_name"

# experience employment types
FULL_TIME = 0
PART_TIME = 1
CONTRACTOR = 2


# database model
def Employee_Db(
        emp_id=None,  # int not null
        photo=None,  # string nullable
        bio=None,  # string nullable
        resume=None,  # string nullable
        name=None,  # string not null
        phone=None,  # string not null
        email=None,  # string not null
        title=None,  # string nullable
        password=None,  # string not null
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
        experience_id=None,
        emp_id=None,
        company_name=None,
        emp_title=None,
        employment_type=None,
        start_date=None,
        end_date=None
):
    return {
        EXPERIENCE_ID: experience_id,
        EMPLOYEE_ID_FK: emp_id,
        EXPERIENCE_COMPANY_NAME: company_name,
        EXPERIENCE_EMP_TITLE: emp_title,
        EXPERIENCE_EMPLOYMENT_TYPE: employment_type,
        EXPERIENCE_START_DATE: start_date,
        EXPERIENCE_END_DATE: end_date
    }
