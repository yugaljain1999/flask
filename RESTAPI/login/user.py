import sqlite3
from flask_restful import Resource, reqparse
from items import Item

class User(Resource):
    TABLE_NAME = 'users'

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    #Here self will replace by cls as we are using existing class named User
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE username=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


class UserRegister(Resource):
    TABLE_NAME = 'users'

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "User with that username already exists."}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES (NULL, ?, ?)".format(table=self.TABLE_NAME)
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201
class ItemsRegister(Resource):


    parser=reqparse.RequestParser()
    parser.add_argument('name',type=str,required=True,help="This field is mandatory")
    parser.add_argument('price',type=float,required=True,help="This field is mandatory")

    def post(self):



        data=ItemsRegister.parser.parse_args()
        if Item.find_by_name(data['name']):
            return {"message":"item already exist"}
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        item_query="INSERT INTO items VALUES(?,?)"
        cursor.execute(item_query,(data['name'],data['price']))
        connection.commit()
        connection.close()
        return {'message':'Items created and inserted into database'}
