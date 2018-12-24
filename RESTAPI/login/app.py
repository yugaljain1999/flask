from flask import Flask
from flask_restful import Api,Resource,request
from flask_jwt import JWT,jwt_required
from security import authenticate,identity
from user import UserRegister,ItemsRegister
from items import Item,Items,list
app=Flask(__name__)
app.secret_key='family'
api=Api(app)
jwt=JWT(app,authenticate,identity)
# Here JWT stands for JSON web token
# Here we have created two terminals get and post where post is used to transfer data to local server and get is used to get the data from post request# RESTful api already use jsonify so we do not need to write jsonify again and again
# Here we will define three classes named as Item,Items and itemlist
# First class names as Item will require jwt means JSON web token to access the post and get requests for eg Facebook comments and sharing post and get other people shared posts
# Second and Third classes do not require jwt
api.add_resource(Item,'/item/<string:name>')
api.add_resource(Items,'/items/<string:clas>')
api.add_resource(list,'/itemlist')
api.add_resource(UserRegister,'/userregister')
api.add_resource(ItemsRegister,'/itemsregister')
app.run(port=5000,debug=True)
