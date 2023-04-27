from flask import jsonify
from entities.models.employee import *
from domain.use_cases.employee_registration import register_new_employee
from domain.use_cases.employee_login import employee_login_use_case
from domain.use_cases.create_session_use_case import *
from domain.utils.dict_utils import get_or_none


def register_employee(request_body):
    employee = Employee_Db(
        -1,
        get_or_none(request_body, EMPLOYEE_photo),
        get_or_none(request_body, EMPLOYEE_BIO),
        get_or_none(request_body, EMPLOYEE_RESUME),
        get_or_none(request_body, EMPLOYEE_NAME),
        get_or_none(request_body, EMPLOYEE_PHONE),
        get_or_none(request_body, EMPLOYEE_EMAIL),
        get_or_none(request_body, EMPLOYEE_TITLE),
        get_or_none(request_body, EMPLOYEE_PASSWORD)
    )
    try:
        emp_id = register_new_employee(employee)
    except Exception as e:
        return jsonify({"error": str(e.args)}), 422
    if emp_id is None:
        return jsonify({"error": "Couldn't create new user please try again"}), 500
    try:
        return jsonify(create_new_session(emp_id, employee[EMPLOYEE_EMAIL], SESSION_TYPE_EMP))
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
        return jsonify(create_new_session(employee[EMPLOYEE_ID], employee[EMPLOYEE_EMAIL], SESSION_TYPE_EMP))
    except Exception as e:
        return jsonify({"error": str(e.args)}), 500
