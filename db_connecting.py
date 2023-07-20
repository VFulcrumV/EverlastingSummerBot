import db_data.db_session as d


def connect():
    d.global_init('db/check_db.db')
