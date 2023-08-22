import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="animal"
)

cursor=db.cursor()
query="create table pets (id int auto_increment primary key,age int not null,gender varchar(200) not null,breed varchar(200) not null,location varchar(200) not null,price int not null);"
cursor.execute(query)

