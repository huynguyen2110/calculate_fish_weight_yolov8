import mysql.connector


def connect_database():
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="fish"
    )
    return db
