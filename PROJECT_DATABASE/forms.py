from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField

class Addform(FlaskForm):
    name=StringField("Enter the name of puppy which you want to add ")
    submit=SubmitField("Submit")

class Delform(FlaskForm):
    id=IntegerField("Enter the id of puppy for which you want to delete puppy")
    submit=SubmitField("Submit")

class Addownerform(FlaskForm):
    name=StringField("Add owner to any Puppy")
    puppy_id=IntegerField("Enter the id of puppy")
    submit=SubmitField("Submit")
