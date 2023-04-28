from flask import jsonify
from entities.models.employee import *
from entities.models.company import *
from domain.use_cases.employee_registration_use_case import employee_registration_use_case
from domain.use_cases.company_registration_use_case import company_registration_use_case
from domain.use_cases.employee_login_use_case import employee_login_use_case
from domain.use_cases.company_login_use_case import company_login_use_case
from domain.use_cases.create_session_use_case import *
from domain.utils.dict_utils import get_or_none


def register_employee(request_body):
    employee = Employee_Db(
        -1,
        get_or_none(request_body, EMPLOYEE_PHOTO),
        get_or_none(request_body, EMPLOYEE_BIO),
        get_or_none(request_body, EMPLOYEE_RESUME),
        get_or_none(request_body, EMPLOYEE_NAME),
        get_or_none(request_body, EMPLOYEE_PHONE),
        get_or_none(request_body, EMPLOYEE_EMAIL),
        get_or_none(request_body, EMPLOYEE_TITLE),
        get_or_none(request_body, EMPLOYEE_PASSWORD)
    )
    try:
        emp_id = employee_registration_use_case(employee)
    except Exception as e:
        return jsonify({"error": str(e.args)}), 422
    if emp_id is None:
        return jsonify({"error": "Couldn't create new user please try again"}), 500
    try:
        return jsonify(create_session_use_case(emp_id, employee[EMPLOYEE_EMAIL], EMPLOYEE_SESSION_TABLE_NAME))
    except Exception as e:
        return jsonify({"error": str(e.args)}), 500


def register_company(request_body):
    company = Company_Db(
        -1,
        get_or_none(request_body, COMPANY_LOGO),
        get_or_none(request_body, COMPANY_NAME),
        get_or_none(request_body, COMPANY_INDUSTRY),
        get_or_none(request_body, COMPANY_WEBSITE),
        get_or_none(request_body, COMPANY_ABOUT),
        get_or_none(request_body, COMPANY_EMAIL),
        get_or_none(request_body, COMPANY_FACEBOOK_PAGE),
        get_or_none(request_body, COMPANY_PASSWORD)
    )
    try:
        company_id = company_registration_use_case(company)
    except Exception as e:
        return jsonify({"error": str(e.args)}), 422
    if company_id is None:
        return jsonify({"error": "Couldn't create new company please try again"}), 500
    try:
        return jsonify(create_session_use_case(company_id, company[EMPLOYEE_EMAIL], COMPANY_SESSION_TABLE_NAME))
    except Exception as e:
        return jsonify({"error": str(e.args)}), 500


def login_employee(request_body):
    email = get_or_none(request_body, EMPLOYEE_EMAIL)
    password = get_or_none(request_body, EMPLOYEE_PASSWORD)
    try:
        employee = employee_login_use_case(email, password)
    except Exception as e:
        return jsonify({"error": str(e.args)}), 422
    if employee is None:
        return jsonify({"error": "UnKnown error occurred please try again"}), 500
    try:
        return jsonify(
            create_session_use_case(employee[EMPLOYEE_ID], employee[EMPLOYEE_EMAIL], EMPLOYEE_SESSION_TABLE_NAME))
    except Exception as e:
        return jsonify({"error": str(e.args)}), 500


def login_company(request_body):
    email = get_or_none(request_body, COMPANY_EMAIL)
    password = get_or_none(request_body, COMPANY_PASSWORD)
    try:
        company = company_login_use_case(email, password)
    except Exception as e:
        return jsonify({"error": str(e.args)}), 422
    if company is None:
        return jsonify({"error": "UnKnown error occurred please try again"}), 500
    try:
        return jsonify(create_session_use_case(company[COMPANY_ID], company[COMPANY_EMAIL], COMPANY_SESSION_TABLE_NAME))
    except Exception as e:
        return jsonify({"error": str(e.args)}), 500
