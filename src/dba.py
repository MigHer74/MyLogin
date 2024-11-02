import sqlite3


def connect():
    connection = sqlite3.connect("./db/logins.db")
    return connection


def existing_table():
    sqldb = """CREATE TABLE IF NOT EXISTS users (
    user_id TEXT NOT NULL,
    user_name TEXT NOT NULL,
    user_password TEXT NOT NULL,
    CONSTRAINT pk_user_id PRIMARY KEY (user_id)
    );"""

    condb = connect()
    curdb = condb.cursor()
    curdb.execute(sqldb)
    condb.commit()
    condb.close()
