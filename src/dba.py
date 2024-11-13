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


def retrieve_info(dataId=None):
    condb = connect()
    curdb = condb.cursor()

    if dataId:
        sqldb = f"""SELECT user_id, user_name FROM users WHERE
        user_id = '{dataId}'"""
        datdb = curdb.execute(sqldb).fetchone()
    else:
        sqldb = "SELECT user_id, user_name FROM users ORDER BY user_id"
        datdb = curdb.execute(sqldb).fetchall()

    condb.close()
    return datdb


def insert_info(dataId, dataName, dataPassword):
    sqldb = f"""INSERT INTO 'users' VALUES('{dataId}', '{dataName}',
    '{dataPassword}')"""

    condb = connect()
    curdb = condb.cursor()
    curdb.execute(sqldb)
    condb.commit()
    condb.close()


def update_info(dataId, dataName):
    sqldb = f"""UPDATE 'users' SET user_name = '{dataName}'
    WHERE user_id = '{dataId}'"""

    condb = connect()
    curdb = condb.cursor()
    curdb.execute(sqldb)
    condb.commit()
    condb.close()


def delete_info(dataId):
    sqldb = f"DELETE FROM 'users' WHERE user_id = '{dataId}';"

    condb = connect()
    curdb = condb.cursor()
    curdb.execute(sqldb)
    condb.commit()
    condb.close()
