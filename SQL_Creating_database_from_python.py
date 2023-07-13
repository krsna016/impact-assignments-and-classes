import mysql.connector
MyDatabase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'A1nurag_P16areek'
)
MyCursor = MyDatabase.cursor()
# Creating database
MyCursor.execute("CREATE DATABASE if not exists database_3")
MyDatabase.close()