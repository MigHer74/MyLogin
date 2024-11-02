from pathlib import Path
from src import dba as db


def verify_storage():
    dbFolder = "db"
    dbFile = "logins.db"

    if not Path(dbFolder).is_dir():
        Path.mkdir("db")

    if not Path(dbFile).is_file():
        db.existing_table()
