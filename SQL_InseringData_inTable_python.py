import mysql.connector
MyDatabase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'A1nurag_P16areek'
)
MyCursor = MyDatabase.cursor()
# Creating database
MyCursor.execute("insert into database_3.MyFirstTable values(123,'Anurag',5559.9,550,'Pareek')") # In SQL name showed be written inside single quotes
# need to this command in order to reflect data into the database:
MyDatabase.commit()
MyDatabase.close()