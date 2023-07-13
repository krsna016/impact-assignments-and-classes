import mysql.connector
MyDatabase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'A1nurag_P16areek'
)
MyCursor = MyDatabase.cursor()
# Creating database
MyCursor.execute("CREATE TABLE if not exists database_3.MyFirstTable(c1 INT,c2 VARCHAR(50),c3 FLOAT,c4 INT,c5 VARCHAR(60))")
MyDatabase.close()