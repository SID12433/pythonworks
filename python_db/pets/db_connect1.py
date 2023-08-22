import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    username="root",
    password="Password@123"
)

cursor=db.cursor()
query="create database animal"
cursor.execute(query)
