from get_connection import db_connect

db=db_connect(password="Password@123",database="animal")

cursor=db.cursor()
query="""select * from pets"""
cursor.execute(query)

records=cursor.fetchall()  #get(retrieve) all records
for rec in records:
    print(rec)