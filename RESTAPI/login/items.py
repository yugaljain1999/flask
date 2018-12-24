from flask_restful import Resource
from flask_jwt import jwt_required
import sqlite3
# Here now we have separated the classes of items in separate file named as items.py and will try to creating a database for items also like we did for username and user_id recently

class Item(Resource):


    @jwt_required()
    def get(self,name):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        select_query="SELECT * FROM items WHERE name=?"
        result=cursor.execute(select_query,(name,))
        row=result.fetchone()
        connection.close()
        if row:
            return {'item':{'name':row[0],'price':row[1]}}
        return {"message":"item doesn't exists"}


# Here note that common error in web application is not 404 it is 200 instead if we donot specify 404
    @classmethod
    def find_by_name(cls,name):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        select_query="SELECT * FROM items WHERE name=?"
        result=cursor.execute(select_query,(name,))
        row=result.fetchone()
        if row:
            user=cls(*row)
        else:
            user=None
        connection.close()
        return user

    def post(self,name):
        item={'name':name,'price':17000}
        items.append(item)
        return item,201
    @classmethod
    def insert(cls,item):
        connection=sqlite3.connect()
        cursor=connection.cursor()
        insert_query="INSERT INTO items VALUES(?,?)"
        cursor.execute(insert_query,(item['name'],item['price']))
        connection.commit()
        connection.close()
        
        
        
    def delete(self,name):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        delete_query="DELETE FROM items WHERE name=?"
        result=cursor.execute(delete_query,(name,))
        connection.commit()
        connection.close()
        return {'message':'Item deleted from given list'}
    def put(self,name):
        data=request.get_json()
        item=next(filter(lambda x: x['name']==name,items),None)
        # After acheiving none condition it doesn't matter that how many times we are calling put method
        if item is None:
            item={'name':name,'price':18000}
            items.append(item)
        else:
            item.update(data)    # Here we are updating the value of price if name is same because name already eist otherwise name will also has to be changed
        return item,{'message':'item is updated'}
class Items(Resource):
    def get(self,clas):
        item=next(filter(lambda x: x['cla']==clas,items),None)
        # Here next means first value of list
        return {'item':item},200 if item else 400
    def post(self,clas):
        item={'clas':clas,'MRP':18000,'Rollno':63}
        items.append(item)
        return item,202
class list(Resource):
    def get(self):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        select_query="SELECT * FROM items"
        row=cursor.execute(select_query)
        connection.close()
        if row:
            return {"items":items}
        return {'message':"items doesn't exist"}
