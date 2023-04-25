# employee variable names
EMPLOYEE_ID = "id"
EMPLOYEE_photo = "photo"
EMPLOYEE_BIO = "bio"
EMPLOYEE_RESUME = "resume"
EMPLOYEE_NAME = "name"
EMPLOYEE_PHONE = "phone"
EMPLOYEE_EMAIL = "email"
EMPLOYEE_TITLE = "title"
EMPLOYEE_PASSWORD = "password"


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
        password  # string not null
):
    return {
        EMPLOYEE_ID: emp_id,
        EMPLOYEE_photo: photo,
        EMPLOYEE_BIO: bio,
        EMPLOYEE_RESUME: resume,
        EMPLOYEE_NAME: name,
        EMPLOYEE_PHONE: phone,
        EMPLOYEE_EMAIL: email,
        EMPLOYEE_TITLE: title,
        EMPLOYEE_PASSWORD: password
    }


# API model
def Employee_API(
        photo,  # string nullable
        bio,  # string nullable
        resume,  # string nullable
        name,  # string not null
        phone,  # string not null
        email,  # string not null
        title,  # string nullable
):
    return {
        EMPLOYEE_photo: photo,
        EMPLOYEE_BIO: bio,
        EMPLOYEE_RESUME: resume,
        EMPLOYEE_NAME: name,
        EMPLOYEE_PHONE: phone,
        EMPLOYEE_EMAIL: email,
        EMPLOYEE_TITLE: title
    }


def map_to_employee_api(employee_db):
    return Employee_API(
        photo=employee_db[EMPLOYEE_photo],
        bio=employee_db[EMPLOYEE_BIO],
        resume=employee_db[EMPLOYEE_RESUME],
        name=employee_db[EMPLOYEE_NAME],
        phone=employee_db[EMPLOYEE_PHONE],
        email=employee_db[EMPLOYEE_EMAIL],
        title=employee_db[EMPLOYEE_TITLE]
    )
