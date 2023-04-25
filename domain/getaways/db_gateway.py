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
        print(f"An error occurred while connecting the database\n{errno}")
    return db


def make_db_query(query):
    db = open_db_connection()
    if db is None:
        return
    cursor = db.cursor(db)
    try:
        cursor.execute(query)
        db.commit()
    except:
        print(f"couldn't make the db operation due to an error\n{errno}")
    finally:
        cursor.close
        db.close()
