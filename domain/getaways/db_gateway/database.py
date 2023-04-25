import traceback

import mysql.connector as mysqldb


def open_db_connection():
    db = None
    try:
        db = mysqldb.connect(
            host="host",
            user="user",
            password="pass",
            database="db"
        )
    except:
        print(f"An error occurred while connecting the database\n{traceback.TracebackException}")
    return db
