from get_connection import db_connect

db=db_connect(password="Password@123",database="animal")

cursor=db.cursor()
query="""select price from pets where breed="mastiff";"""
cursor.execute(query)

records=cursor.fetchall()
print(records)