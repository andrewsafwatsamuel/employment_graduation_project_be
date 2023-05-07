from flask import jsonify

from domain.use_cases.add_new_job_listing_use_case import add_new_job_listing_use_case
from domain.use_cases.get_session_by_token_use_case import *
from domain.use_cases.apply_for_job_use_case import *
from domain.use_cases.search_job_by_company_or_title_use_case import *
from domain.use_cases.get_all_jobs_by_company_id_use_case import *
from domain.use_cases.toggle_job_listing_status_use_case import *
from domain.utils.dict_utils import get_or_none
from domain.utils.validation_utils import has_valid_session
from entities.constants.constants import AUTH_TOKEN
from entities.models.job_listing import *


def create_job_listing(request_body, request_headers):
    auth_token = get_or_none(request_headers, AUTH_TOKEN)
    if auth_token is None:
        return jsonify({"message": "unauthorized"}), 401
    try:
        session = get_session_by_token_use_case(auth_token, COMPANY_SESSION_TABLE_NAME)
    except Exception as e:
        return jsonify({"message": e.args}), 401
    if not has_valid_session(session):
        return jsonify({"message": "unauthorized"}), 401
    job_listing_db = Job_Listing_Db(
        -1,
        get_or_none(session, OWNER_ID),
        get_or_none(request_body, JOB_LISTING_EXP_LEVEL),
        get_or_none(request_body, JOB_LISTING_TITLE),
        get_or_none(request_body, JOB_LISTING_STATUS),
        get_or_none(request_body, JOB_LISTING_DESCRIPTION)
    )
    try:
        inserted_successfully = add_new_job_listing_use_case(job_listing_db) is not None
    except Exception as e:
        return jsonify({"message": str(e.args)}), 400
    return (jsonify({"message": "Job created successfully"}), 200) if inserted_successfully else (jsonify(
        {"message": "Unexpected error"}), 400)


def search_job_by_company_or_title(request_args):
    search_key = get_or_none(request_args, "searchKey")
    try:
        jobs = search_job_by_company_or_title_use_case(search_key)
    except Exception as e:
        return jsonify({"message": str(e.args)}), 500
    return jsonify(jobs if jobs is not None and len(jobs) > 0 else {
        "message": f"No jobs found for '{search_key}' please try another keyword"}), 200


def apply_for_job(request_body, request_headers, use_case=apply_for_job_use_case):
    auth_token = get_or_none(request_headers, AUTH_TOKEN)
    if auth_token is None:
        return jsonify({"message": "unauthorized"}), 401
    try:
        session = get_session_by_token_use_case(auth_token, EMPLOYEE_SESSION_TABLE_NAME)
    except Exception as e:
        return jsonify({"message": e.args}), 401
    if not has_valid_session(session):
        return jsonify({"message": "unauthorized"}), 401
    job_listing_id = get_or_none(request_body, JOB_LISTING_ID_FK)
    job_application = Job_Application_Db(session[OWNER_ID], job_listing_id, None)
    try:
        applied_successfully = use_case(job_application)
    except Exception as e:
        return jsonify({"message": str(e.args)}), 500
    return (jsonify({"message": "Applied successfully"}), 200) if applied_successfully else (jsonify(
        {"message": "Unexpected error"}), 500)


def get_jobs_by_company_id(request_headers, use_case=get_all_jobs_by_company_id_use_case):
    auth_token = get_or_none(request_headers, AUTH_TOKEN)
    if auth_token is None:
        return jsonify({"message": "unauthorized"}), 401
    try:
        session = get_session_by_token_use_case(auth_token, COMPANY_SESSION_TABLE_NAME)
    except Exception as e:
        return jsonify({"message": e.args}), 401
    if not has_valid_session(session):
        return jsonify({"message": "unauthorized"}), 401
    try:
        result = use_case(session[OWNER_ID])
    except Exception as e:
        return jsonify({"message": str(e.args)}), 500
    return jsonify(result if result is not None else {"message", "No Jobs found"}), 200


def update_job_status(request_body, request_headers, use_case=toggle_job_listing_status_use_case):
    auth_token = get_or_none(request_headers, AUTH_TOKEN)
    job_listing_id = get_or_none(request_body, JOB_LISTING_ID)
    if auth_token is None:
        return jsonify({"message": "unauthorized"}), 401
    try:
        session = get_session_by_token_use_case(auth_token, COMPANY_SESSION_TABLE_NAME)
    except Exception as e:
        return jsonify({"message": e.args}), 401
    if not has_valid_session(session):
        return jsonify({"message": "unauthorized"}), 401
    try:
        use_case(job_listing_id, session[OWNER_ID])
    except Exception as e:
        message = str(e.args)
        if message.__contains__("unauthorized"):
            return jsonify({"message": "unauthorized"}), 401
        else:
            return jsonify({"message": str(e.args)}), 500
    return jsonify({"message": "updated successfully "}), 200
