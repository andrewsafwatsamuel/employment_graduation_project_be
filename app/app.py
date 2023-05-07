from flask import Flask, request
from domain.getaways.db_gateway.operations.table_initializer import *
from endpoint_logic.authentication import *
from endpoint_logic.job_listing import *

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


@app.route("/job-listing/add-new-job", methods=['POST'])
def add_new_job():
    return create_job_listing(request.form, request.headers)


@app.route("/job-listing/search", methods=['GET'])
def search_job():
    return search_job_by_company_or_title(request.args)


@app.route("/")
def init():
    return "Hello World!"


if __name__ == "__main__":
    init_db_tables()
    app.run(debug=True)
