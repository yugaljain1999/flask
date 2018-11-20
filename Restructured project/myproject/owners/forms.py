from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField


class Addownerform(FlaskForm):
    name=StringField("Add owner to any Puppy")
    puppy_id=IntegerField("Enter the id of puppy")
    submit=SubmitField("Submit")
