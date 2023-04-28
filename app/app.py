from flask import Flask, request

from domain.getaways.db_gateway.operations.table_initializer import *
from endpoint_logic.authentication import *
from domain.utils.dict_utils import *
from domain.utils.validation_utils import *
from domain.getaways.db_gateway.operations.employee_db_operation import *
from domain.use_cases.has_valid_session_use_case import *

app = Flask(__name__)


@app.route("/employees/register", methods=['POST'])
def register_employee_endpoint():
    return register_employee(request.form)


@app.route("/companies/register", methods=['POST'])
def register_company_endpoint():
    return register_company(request.form)


@app.route("/employees/login", methods=['POST'])
def login_employee_endpoint():
    return login_employee(request.form)


@app.route("/companies/login", methods=['POST'])
def login_company_endpoint():
    return login_company(request.form)


@app.route("/employees/profile", methods=['GET'])
def employee_profile_info_endpoint():
    auth_token = get_or_none(request.headers, 'Authorization')  # make usre
    print(auth_token)
    try:
        current_session = has_valid_session_use_case(auth_token, EMPLOYEE_SESSION_TABLE_NAME)
        print(current_session)
    except Exception as e:
        return jsonify({"Message": e.args}), 401
    if not current_session.get("is_valid"):
        return jsonify({"Message": "Not Authorized"}), 401
    try:
        employee = retrieve_employee_by_email(current_session.get(OWNER_EMAIL))
    except:
        return jsonify({"Message": "Error while retrieving employee data"}), 500
    if employee is None:
        return jsonify({"Message": "Error while retrieving employee data (employee is none)"}), 500
    else:
        return jsonify({
            EMPLOYEE_NAME: employee.get(EMPLOYEE_NAME),
            EMPLOYEE_EMAIL: employee.get(EMPLOYEE_EMAIL),
            EMPLOYEE_PHONE: employee.get(EMPLOYEE_PHONE),
            EMPLOYEE_TITLE: employee.get(EMPLOYEE_TITLE),
            EMPLOYEE_PHOTO: employee.get(EMPLOYEE_PHOTO),
            EMPLOYEE_RESUME: employee.get(EMPLOYEE_RESUME),
            EMPLOYEE_BIO: employee.get(EMPLOYEE_BIO),
            "experiences": []
        })


@app.route("/")
def init():
    return "Hello World!"


if __name__ == "__main__":
    init_db_tables()
    app.run(debug=True)
