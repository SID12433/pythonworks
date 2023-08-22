from get_connection import db_connect

class PetsView:
    
    def connect(self):
        db=db_connect(password="Password@123",database="animal")
        return db
    
    def get(self):
        db=self.connect()
        cursor=db.cursor()
        query="""select * from pets"""
        cursor.execute(query)
        qs=cursor.fetchall()
        return qs
    
    def retrieve(self,id):
        db=self.connect()
        cursor=db.cursor()
        query=f"select * from pets where id={id}"
        cursor.execute(query)
        qs=cursor.fetchone()
        return qs
        
    def post(self,*args,**kwargs):
        db=self.connect()
        cursor=db.cursor()
        query="insert into pets(age,gender,breed,location,price)""values(%s,%s,%s,%s,%s)"
        data=tuple(i for i in kwargs.values())
        cursor.execute(query,data)
        db.commit()
        
    def destroy(self,id):
        db=self.connect()
        cursor=db.cursor()
        query=f"delete from pets where id ={id}"
        cursor.execute(query)
        db.commit()
        return "deleted success"
    
    def update(self,id,*args,**kwargs):
        db=self.connect()
        cursor=db.cursor()
        data=list(i for i in kwargs.values())
        data.append(id)
        query="update pets set age=%s,gender=%s,breed=%s,location=%s,price=%s where id=%s"
        cursor.execute(query,data)
        db.commit()
        return "updation success"
    
pv=PetsView()
# print(pv.get())
# print(pv.retrieve(2))
# pv.post(age=5,gender="male",breed="german",location="kannur",price=30000)
# print(pv.destroy(2))
print(pv.update(id=1,age=7,gender="female",breed="tibetian mastiff",location="kannur",price=50000))