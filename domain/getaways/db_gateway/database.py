import mysql.connector as mysqldb


def open_db_connection():
    db = None
    try:
        db = mysqldb.connect(
            host="localhost",
            user="root",
            password="123.Abcd",
            database="hire_wire_db"
        )
    except Exception as e:
        print(f"An error occurred while connecting the database\n{e.__cause__}")
    return db
