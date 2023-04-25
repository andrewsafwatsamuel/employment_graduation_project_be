from flask import Flask
from domain.getaways.db_gateway import *
from domain.getaways.table_creation_queries import *

app = Flask(__name__)

if __name__ == '__main__':
    make_db_query(empoyee_creation_query)
    app.run()


@app.route('/')
def init():
    return 'Hello World!'
