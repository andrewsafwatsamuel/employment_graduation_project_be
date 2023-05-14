from domain.use_cases.get_employee_profile_use_case import *
from flask import jsonify


def get_employee_profile(emp_id, use_case=get_employee_profile_use_case):
    try:
        return jsonify(use_case(emp_id)), 200
    except Exception as e:
        return jsonify({"message": str(e.args)}), 500
