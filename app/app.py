from flask import Flask, request

from domain.getaways.db_gateway.operations.table_initializer import *
from endpoint_logic.authentication import *

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


@app.route("/")
def init():
    return "Hello World!"


if __name__ == "__main__":
    init_db_tables()
    app.run(debug=True)

# query to retrieve session by token
# query to delete sessions attached to email
# delete entry by token

# use case to check have valid toke that validate token is not blank or null
# token is not expired
# if okay proceed else throw exception with 401 response
