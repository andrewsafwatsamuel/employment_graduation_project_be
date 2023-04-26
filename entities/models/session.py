OWNER_ID = "owner_id"
Auth_TOKEN = "auth_token"
REFRESH_TOKEN = "refresh_token"
OWNER_EMAIL = "email"
CREATED_AT = "created_at"
EMPLOYEE_SESSION_TABLE_NAME = "employee_session"
COMPANY_SESSION_TABLE_NAME = "company_session"


def Session_Db(
        owner_id,
        auth_token,
        refresh_token,
        owner_email,
        created_at
):
    return {
        OWNER_ID: owner_id,
        Auth_TOKEN: auth_token,
        REFRESH_TOKEN: refresh_token,
        OWNER_EMAIL: owner_email,
        CREATED_AT: created_at
    }
