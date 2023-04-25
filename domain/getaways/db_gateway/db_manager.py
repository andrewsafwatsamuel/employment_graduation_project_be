from domain.getaways.db_gateway.database import *


def make_db_query(query):
    db = open_db_connection()
    if db is None:
        return
    cursor = db.cursor(db)
    try:
        cursor.execute(query)
        db.commit()
    except:
        print(f"couldn't make the db operation due to an error\n{traceback.TracebackException}")
    finally:
        cursor.close
        db.close()
