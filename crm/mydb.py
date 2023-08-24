import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = ''
)


cursorObject = dataBase.cursor()

#   Create a DataBase 
cursorObject.execute("CREATE DATABASE crm_django_mysql")

print("All Done!")