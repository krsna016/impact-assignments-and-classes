import mysql.connector
MyDatabase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'A1nurag_P16areek'
)
MyCursor = MyDatabase.cursor()
# Creating database
MyCursor.execute("insert into database_3.MyFirstTable values(123,'Anurag',5559.9,550,'Pareek')")
MyCursor.execute("insert into database_3.MyFirstTable values(123,'Anurag',5559.9,550,'Pareek')")
MyCursor.execute("insert into database_3.MyFirstTable values(123,'Anurag',5559.9,550,'Pareek')")
MyCursor.execute("insert into database_3.MyFirstTable values(123,'Anurag',5559.9,550,'Pareek')")
MyCursor.execute("insert into database_3.MyFirstTable values(123,'Anurag',5559.9,550,'Pareek')")
MyCursor.execute("insert into database_3.MyFirstTable values(123,'Anurag',5559.9,550,'Pareek')")
MyCursor.execute("insert into database_3.MyFirstTable values(123,'Anurag',5559.9,550,'Pareek')")

# MyCursor.execute("select * from database_3.MyFirstTable")
MyCursor.execute("select c1,c5 from database_3.MyFirstTable") # For some specific column
for i in MyCursor.fetchall():
    print(i)
MyDatabase.close()