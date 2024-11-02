import sqlite3


def connect():
    connection = sqlite3.connect("./db/logins.db")
    return connection
