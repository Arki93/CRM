import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '12memoreX-!'
    )

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE CRM_TEST")

print('database created')