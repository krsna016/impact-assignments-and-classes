import mysql.connector
MyDatabase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'A1nurag_P16areek'
)
MyCursor = MyDatabase.cursor()
# Creating database
MyCursor.execute("select * from database_3.MyFirstTable")
for i in MyCursor.fetchall(): # Traversing the result
    print(i)
MyDatabase.close()