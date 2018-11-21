from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,EqualTo,Email
from wtforms import ValidationError
class LoginForm(FlaskForm):
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    submit=SubmitField("Submit")

class RegistrationForm(FlaskForm):
    email=StringField("Email",validators=[DataRequired(),Email()])
    username=StringField("Username",validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired(),EqualTo("pass_confirm",message="Password should be correct")])
    pass_confirm=PasswordField("Password",validators=[DataRequired()])
    submit=SubmitField("Submit")
    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Your email has already benn registered")

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Your username is set")
