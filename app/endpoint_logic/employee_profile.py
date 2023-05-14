from domain.use_cases.get_employee_profile_use_case import *
from flask import jsonify


def get_employee_profile(emp_id, use_case=get_employee_profile_use_case):
    try:
        employee = use_case(emp_id)
        return (jsonify(employee), 200) if employee is not None else (jsonify({"message": "Employee not found"}), 404)
    except Exception as e:
        return jsonify({"message": str(e.args)}), 500
