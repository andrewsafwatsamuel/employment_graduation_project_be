from flask import jsonify

from domain.use_cases.add_new_job_listing_use_case import add_new_job_listing_use_case
from domain.use_cases.get_session_by_token_use_case import *
from domain.use_cases.search_job_by_company_or_title_use_case import *
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
