from domain.use_cases.get_employee_profile_use_case import *
from domain.use_cases.get_session_by_token_use_case import *
from domain.utils.validation_utils import has_valid_session
from domain.utils.dict_utils import get_or_none
from domain.use_cases.update_employee_profile_use_case import update_employee_profile_use_case
from domain.use_cases.add_experience_use_case import add_experience_use_case
from domain.use_cases.remove_experience_use_case import remove_experience_use_case
from domain.use_cases.update_employee_password_use_case import update_employee_password_use_case
from flask import jsonify
from entities.constants.constants import AUTH_TOKEN
from entities.models.employee import *


def get_employee_profile(emp_id, use_case=get_employee_profile_use_case):
    try:
        employee = use_case(emp_id)
        return (jsonify(employee), 200) if employee is not None else (jsonify({"message": "Employee not found"}), 404)
    except Exception as e:
        return jsonify({"message": str(e.args)}), 500


def update_employee_profile(
        request_headers,
        request_body,
        use_case=update_employee_profile_use_case
):
    session = get_user_session(request_headers, EMPLOYEE_SESSION_TABLE_NAME)
    if get_or_none(session, "message") is not None:
        return jsonify(session), 401
    emp_db = Employee_Db(
        emp_id=session[OWNER_ID],
        bio=get_or_none(request_body, EMPLOYEE_BIO),
        name=get_or_none(request_body, EMPLOYEE_NAME),
        phone=get_or_none(request_body, EMPLOYEE_PHONE),
        email=get_or_none(request_body, EMPLOYEE_EMAIL),
        title=get_or_none(request_body, EMPLOYEE_TITLE)
    )
    emp_db.pop(EMPLOYEE_PASSWORD)
    emp_db.pop(EXPERIENCE_TABLE_NAME)
    try:
        updated_successfully = use_case(emp_db)
    except Exception as e:
        return jsonify({"message": str(e.args)}), 400
    json = jsonify(emp_db) if updated_successfully else jsonify({"message": "Nothing updated"})
    return json, 200


def add_new_experience(
        request_headers,
        request_body,
        use_case=add_experience_use_case
):
    session = get_user_session(request_headers, EMPLOYEE_SESSION_TABLE_NAME)
    if get_or_none(session, "message") is not None:
        return jsonify(session), 401
    experience = Experience_Db(
        emp_id=session[OWNER_ID],
        company_name=get_or_none(request_body, EXPERIENCE_COMPANY_NAME),
        emp_title=get_or_none(request_body, EXPERIENCE_EMP_TITLE),
        employment_type=get_or_none(request_body, EXPERIENCE_EMPLOYMENT_TYPE),
        start_date=get_or_none(request_body, EXPERIENCE_START_DATE),
        end_date=get_or_none(request_body, EXPERIENCE_END_DATE)
    )
    try:
        experience_id = use_case(experience)
    except Exception as e:
        return jsonify({"message": str(e.args)}), 400
    experience.update({EXPERIENCE_ID: experience_id})
    json = jsonify(experience) if experience_id is not None else jsonify({"message": "Experience is not added"})
    return json, 200


def remove_experience(
        request_headers,
        request_body,
        use_case=remove_experience_use_case,
        employee_profile=get_employee_profile_use_case
):
    session = get_user_session(request_headers, EMPLOYEE_SESSION_TABLE_NAME)
    if get_or_none(session, "message") is not None:
        return jsonify(session), 401
    try:
        updated_successfully = use_case(session[OWNER_ID], get_or_none(request_body, EXPERIENCE_ID))
    except Exception as e:
        return jsonify({"message": str(e.args)}), 400
    if updated_successfully:
        try:
            employee_profile = employee_profile(session[OWNER_ID])
        except Exception as e:
            return jsonify({"message": str(e.args)}), 400
        return jsonify(employee_profile), 200
    else:
        return jsonify({"message": "Experience is not removed"}), 200


def update_employee_password(
        request_headers,
        request_body,
        use_case=update_employee_password_use_case
):
    session = get_user_session(request_headers, EMPLOYEE_SESSION_TABLE_NAME)
    if get_or_none(session, "message") is not None:
        return jsonify(session), 401
    try:
        updated_successfully = use_case(
            session[OWNER_EMAIL],
            get_or_none(request_body, "old-password"),
            get_or_none(request_body, "new-password")
        )
    except Exception as e:
        return jsonify({"message": str(e.args)}), 400
    return jsonify(
        {"message": "Password successfully updated" if updated_successfully else "Password not updated"}), 200


def get_user_session(request_headers, table, session_use_case=get_session_by_token_use_case):
    auth_token = get_or_none(request_headers, AUTH_TOKEN)
    if auth_token is None:
        return {"message": "unauthorized"}
    try:
        session = session_use_case(auth_token, table)
    except Exception as e:
        return {"message": str(e.args)}
    if not has_valid_session(session):
        return {"message": "unauthorized"}
    return session
