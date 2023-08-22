import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123"
)

cursor=db.cursor()
query="""create database phones"""
cursor.execute(query)