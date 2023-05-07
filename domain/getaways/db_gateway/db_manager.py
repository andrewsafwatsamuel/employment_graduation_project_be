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


def insert_on_many_tables(operation):
    db = open_db_connection()
    row_id = None
    if db is None:
        return row_id
    cursor = db.cursor(db)
    try:
        row_id = operation(db, cursor)
    finally:
        cursor.close()
        db.close()
    return row_id


def query_single_value(query, where_args):
    db = open_db_connection()
    result = None
    if db is None:
        return result
    cursor = db.cursor(db)
    try:
        cursor.execute(query.format(*where_args))
        result = cursor.fetchone()
    finally:
        cursor.close()
        db.close()
    return result


def query_multiple_values(query, where_args):
    db = open_db_connection()
    result = None
    if db is None:
        return result
    cursor = db.cursor(db)
    try:
        cursor.execute(query.format(*where_args))
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(row)
    finally:
        cursor.close()
        db.close()
    return result


def delete_db_entries(query, where_args):
    db = open_db_connection()
    row_count = None
    if db is None:
        return row_count
    cursor = db.cursor(db)
    try:
        cursor.execute(query.format(*where_args))
        db.commit()
        row_count = cursor.rowcount
    finally:
        cursor.close()
        db.close()
    return row_count
