from get_connection import db_connect

class MobileView:
    
    def connect(self):
        db=db_connect(password="Password@123",database="phones")
        return db
    
    def get(self):
        db=self.connect()
        cursor=db.cursor()
        query="""select * from mobiles"""
        cursor.execute(query)
        qs=cursor.fetchall()
        return qs
    
mob=MobileView()
print(mob.get())
