from flask import Flask, request
from domain.getaways.db_gateway.operations.table_initializer import *
from endpoint_logic.authentication import *

app = Flask(__name__)


@app.route("/employees/register", methods=['POST'])
def register_employee_endpoint():
    return register_employee(request.form)


@app.route("/")
def init():
    return "Hello World!"


if __name__ == "__main__":
    init_db_tables()
    app.run(debug=True)
