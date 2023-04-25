from flask import Flask
from domain.getaways.db_gateway.table_initializer import *

app = Flask(__name__)

if __name__ == '__main__':
    init_db_tables()
    app.run()


@app.route('/')
def init():
    return 'Hello World!'
