import bcrypt
from pathlib import Path
from PIL import ImageTk, Image
from src import dba as db


def verify_storage():
    dbFolder = "db"
    dbFile = "logins.db"

    if not Path(dbFolder).is_dir():
        Path.mkdir("db")

    if not Path(dbFile).is_file():
        db.existing_table()


def image_resize(infoPic, infoWidth, infoHeight):
    imgTemp = Image.open(infoPic)
    imgTemp = imgTemp.resize((infoWidth, infoHeight))
    imgFin = ImageTk.PhotoImage(imgTemp)

    return imgFin


def hashing_password(dataPassword):
    passwordHashed = bcrypt.hashpw(dataPassword.encode('utf-8'),
                                   bcrypt.gensalt())
    passwordStorage = passwordHashed.decode('utf-8')

    return passwordStorage
