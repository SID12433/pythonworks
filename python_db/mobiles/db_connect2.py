from get_connection import db_connect

db=db_connect(password="Password@123",database="phones")

cursor=db.cursor()
query="""create table mobiles(id int auto_increment primary key,name varchar(100) not null,brand varchar(200)not null,spec varchar(200)not null,price int not null)"""
cursor.execute(query)
