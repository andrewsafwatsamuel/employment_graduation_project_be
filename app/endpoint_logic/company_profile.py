from domain.use_cases.get_company_profile_use_case import *
from flask import jsonify


def get_company_profile(company_id, use_case=get_company_profile_use_case):
    try:
        company = use_case(company_id)
        return (jsonify(company), 200) if company is not None else (jsonify({"message": "Company not found"}), 404)
    except Exception as e:
        return jsonify({"message": str(e.args)}), 500
