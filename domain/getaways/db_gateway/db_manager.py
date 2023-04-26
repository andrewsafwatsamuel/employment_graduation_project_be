from domain.getaways.db_gateway.database import *


def make_db_query(query):
    db = open_db_connection()
    if db is None:
        return
    cursor = db.cursor(db)
    try:
        cursor.execute(query)
        db.commit()
    finally:
        cursor.close()
        db.close()


def insert_new_record(query, values):
    db = open_db_connection()
    row_id = None
    if db is None:
        return row_id
    cursor = db.cursor(db)
    try:
        cursor.execute(query, values)
        db.commit()
        row_id = cursor.lastrowid
    finally:
        cursor.close()
        db.close()
    return row_id
