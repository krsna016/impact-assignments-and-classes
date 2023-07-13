import mysql.connector # Inorder to connect python and SQL usie this library

# Making connection between MySQL and python
# System Configuration:
MyDatabase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'A1nurag_P16areek'
)
print(MyDatabase) # Show our connection
# Making cursor in order to update/modify/traverse data in database
MyCursor = MyDatabase.cursor()
MyCursor.execute("SHOW DATABASES") # To call any command write it in parenthesis
for i in MyCursor:
    print(i)
