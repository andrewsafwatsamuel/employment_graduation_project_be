from flask import Flask, request
from domain.getaways.db_gateway.operations.table_initializer import *
from endpoint_logic.authentication import *
from endpoint_logic.job_listing import *
from endpoint_logic.employee_profile import *
from endpoint_logic.company_profile import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


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


@app.route("/employees/<emp_id>", methods=['get'])
def get_employee_profile_end_point(emp_id):
    return get_employee_profile(emp_id)


@app.route("/companies/<company_id>", methods=['get'])
def get_company_profile_end_point(company_id):
    return get_company_profile(company_id)


@app.route("/job-listing/add-new-job", methods=['POST'])
def add_new_job():
    return create_job_listing(request.form, request.headers)


@app.route("/job-listing/search", methods=['GET'])
def search_job():
    return search_job_by_company_or_title(request.args)


@app.route("/job-listing/apply", methods=['POST'])
def search_application():
    return apply_for_job(request.form, request.headers)


@app.route("/companies/published-jobs", methods=['GET'])
def getJobs_for_a_company():
    return get_jobs_by_company_id(request.headers)


@app.route("/job-listing/update-status", methods=['PUT'])
def update_job_listing_status():
    return update_job_status(request.form, request.headers)


@app.route("/job-listing/update-application-status", methods=['PUT'])
def update_job_application_status_end_point():
    return update_application_status(request.form, request.headers)


@app.route("/job-listing/<job_listing_id>", methods=['PUT'])
def update_job_listing_endpoint(job_listing_id):
    return update_job_listing(request.form, request.headers, job_listing_id)


@app.route("/job-listing/<job_listing_id>/applications", methods=['GET'])
def get_job_applications_end_point(job_listing_id):
    return get_job_applications(request.headers, job_listing_id)


@app.route("/")
def init():
    return "Hello World!"


if __name__ == "__main__":
    init_db_tables()
    app.run(debug=True)
