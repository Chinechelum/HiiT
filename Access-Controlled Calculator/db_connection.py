import sqlite3

connection = sqlite3.connect("usersdetails.db")

# # Adding Data to the SQLite Database
cursor = connection.cursor()
cursor.execute("CREATE TABLE userprofile (username TEXT, password TEXT)")
connection.commit()
connection.close()