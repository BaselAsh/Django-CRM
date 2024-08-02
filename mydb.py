import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Pasel 2016"
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE baselco")

print("All Alright")
# The code ran but didn't check if it works but it seems like it did