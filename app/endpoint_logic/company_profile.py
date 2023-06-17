from domain.use_cases.get_company_profile_use_case import *
from flask import jsonify
from .utils import get_user_session
from entities.models.session import COMPANY_SESSION_TABLE_NAME, OWNER_ID, OWNER_EMAIL
from domain.use_cases.update_company_profile_use_case import update_company_profile_use_case
from domain.use_cases.add_company_phone_use_case import add_company_phone_use_case
from domain.use_cases.remove_company_phone_use_case import remove_company_phone_use_case
from domain.use_cases.update_company_password_use_case import update_company_password_use_case
from domain.utils.dict_utils import get_or_none
from entities.models.company import *


def get_company_profile(company_id, use_case=get_company_profile_use_case):
    try:
        company = use_case(company_id)
        return (jsonify(company), 200) if company is not None else (jsonify({"message": "Company not found"}), 404)
    except Exception as e:
        return jsonify({"message": str(e.args)}), 500


def update_company_profile(
        request_headers,
        request_body,
        use_case=update_company_profile_use_case
):
    session = get_user_session(request_headers, COMPANY_SESSION_TABLE_NAME)
    if get_or_none(session, "message") is not None:
        return jsonify(session), 401
    company_db = Company_Db(
        company_id=session[OWNER_ID],
        logo=get_or_none(request_body, COMPANY_LOGO),
        name=get_or_none(request_body, COMPANY_NAME),
        industry=get_or_none(request_body, COMPANY_INDUSTRY),
        website=get_or_none(request_body, COMPANY_WEBSITE),
        about=get_or_none(request_body, COMPANY_ABOUT),
        email=get_or_none(request_body, COMPANY_EMAIL),
        fb_page=get_or_none(request_body, COMPANY_FACEBOOK_PAGE)
    )
    company_db.pop(COMPANY_PASSWORD)
    company_db.pop(COMPANY_PHONE_TABLE_NAME)
    try:
        updated_successfully = use_case(company_db)
    except Exception as e:
        return jsonify({"message": str(e.args)}), 400
    json = jsonify(company_db) if updated_successfully else jsonify({"message": "Nothing updated"})
    return json, 200


def add_company_phone(
        request_headers,
        request_body,
        use_case=add_company_phone_use_case
):
    session = get_user_session(request_headers, COMPANY_SESSION_TABLE_NAME)
    if get_or_none(session, "message") is not None:
        return jsonify(session), 401
    try:
        added_successfully = use_case(session[OWNER_ID], get_or_none(request_body, COMPANY_PHONE))
    except Exception as e:
        return jsonify({"message": str(e.args)}), 400
    json = jsonify(
        {COMPANY_PHONE: get_or_none(request_body, COMPANY_PHONE)}) if added_successfully is not None else jsonify(
        {"message": "Phone is not added"})
    return json, 200


def remove_company_phone(
        request_headers,
        request_body,
        use_case=remove_company_phone_use_case,
        company_profile=get_company_profile_use_case
):
    session = get_user_session(request_headers, COMPANY_SESSION_TABLE_NAME)
    if get_or_none(session, "message") is not None:
        return jsonify(session), 401
    try:
        removed_successfully = use_case(session[OWNER_ID], get_or_none(request_body, COMPANY_PHONE))
    except Exception as e:
        return jsonify({"message": str(e.args)}), 400
    if removed_successfully:
        try:
            company_profile = company_profile(session[OWNER_ID])
        except Exception as e:
            return jsonify({"message": str(e.args)}), 400
        return jsonify(company_profile), 200
    else:
        return jsonify({"message": "Phone is not removed"}), 200


def update_company_password(
        request_headers,
        request_body,
        use_case=update_company_password_use_case
):
    session = get_user_session(request_headers, COMPANY_SESSION_TABLE_NAME)
    if get_or_none(session, "message") is not None:
        return jsonify(session), 401
    try:
        updated_successfully = use_case(
            session[OWNER_ID],
            get_or_none(request_body, "old-password"),
            get_or_none(request_body, "new-password")
        )
    except Exception as e:
        return jsonify({"message": str(e.args)}), 400
    return jsonify(
        {"message": "Password successfully updated" if updated_successfully else "Password not updated"}), 200
