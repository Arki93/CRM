import mysql.connector as msc
import os

dataBase = msc.connect(
    host = 'localhost',
    user = os.environ.get("SQL_USER"),
    passwd = os.environ.get("SQL_PASSWD"),
    )

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE CRM_TEST")

print('database created')