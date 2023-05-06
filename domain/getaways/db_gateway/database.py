import mysql.connector as mysqldb


def open_db_connection():
    return mysqldb.connect(
        host="localhost",
        user="root",
        password="123.Abcd",
        database="hire_wire_db"
    )
