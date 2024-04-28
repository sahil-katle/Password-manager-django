import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'pass@123',
)

cursorObject = dataBase.cursor()
cursorObject.execute('CREATE DATABASE password_manager_db')
print('all done.')