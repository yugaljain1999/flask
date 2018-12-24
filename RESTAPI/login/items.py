from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
import sqlite3
# Here now we have separated the classes of items in separate file named as items.py and will try to creating a database for items also like we did for username and user_id recently

class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price',type=float,required=True,help="Can't be blank")



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
        connection.close()
        if row:
            return {'itme':{'name':row[0],'price':row[1]}}

    def post(self,name):
        if self.find_by_name(name):
            return {'message':"This name already exist"}
        data=Item.parser.parse_args()
        item={'name':name,'price':data['price']}
        try:
            Item.insert(item)
        except:
            {'message':"An error occured during inserting an item"}
        return item,201

    @classmethod
    def insert(cls,item):
        connection=sqlite3.connect()
        cursor=connection.cursor()
        insert_query="INSERT INTO items VALUES(?,?)"
        cursor.execute(insert_query,(item['name'],item['price']))
        connection.commit()
        connection.close()


    @jwt_required()
    def delete(self,name):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        delete_query="DELETE FROM items WHERE name=?"
        result=cursor.execute(delete_query,(name,))
        connection.commit()
        connection.close()
        return {'message':'Item deleted from given list'}
    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = self.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']}
        if item is None:
            try:
                Item.insert(updated_item)
            except:
                return {"message": "An error occurred inserting the item."}
        else:
            try:
                Item.update(updated_item)
            except:
                raise
                return {"message": "An error occurred updating the item."}
        return updated_item

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE {table} SET price=? WHERE name=?".format(table=cls.TABLE_NAME)
        cursor.execute(query, (item['price'], item['name']))

        connection.commit()
        connection.close()
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
        result=cursor.execute(select_query)
        items=[]
        for row in result:
            items.append({'name':row[0],'price':row[1]})
        connection.close()
        return {"items":items}
