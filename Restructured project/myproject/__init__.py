import os
from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
app.config['SECRET_KEY']='myfamily'
basedir=os.path.abspath(os.path.dirname(__file__))

app.config['SQLAlchemy_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLAlchemy_TRACK_MODIFICATIONS']=False


db=SQLAlchemy(app)
Migrate(db,app)

from myproject.puppies.views import puppies_blueprint
from myproject.owners.views import owner_blueprint

app.register_blueprint(puppies_blueprint,url_prefix='/puppies')
app.register_blueprint(owner_blueprint,url_prefix='/owners')
