from get_connection import db_connect

db=db_connect(password="Password@123",database="phones")

cursor=db.cursor()
query="""insert into mobiles(name,brand,spec,price) values("note 6 pro","redmi","4gb ram",12000)"""
cursor.execute(query)
db.commit()