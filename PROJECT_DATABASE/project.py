import os
from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import Addform,Delform,Addownerform

app=Flask(__name__)
app.config['SECRET_KEY']='myfamily'
basedir=os.path.abspath(os.path.dirname(__file__))

app.config['SQLAlchemy_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLAlchemy_TRACK_MODIFICATIONS']=False


db=SQLAlchemy(app)
Migrate(db,app)
# Here we are going to create one to one relationship
class Puppy(db.Model):
    __tablename__='puppies'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    owner=db.relationship('Owner',backref='puppy',uselist=False)
    def __init__(self,name):
        self.name=name

    def __repr__(self):
        if self.owner:
            return "The puppy is {} and owner is{}".format(self.name,self.owner.name)
        else:
            return "The puppy is {} and has no owner yet".format(self.name)

db.create_all()
class Owner(db.Model):
    __tablename__='owner'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    puppy_id=db.Column(db.Integer,db.ForeignKey('puppies.id'))
    def __init__(self,name,puppy_id):
        self.name=name
        self.puppy_id=puppy_id

db.create_all()
@app.route('/')
def index():
    return render_template("home.html")

@app.route('/add',methods=['GET','POST'])
def add_pup():
    form=Addform()
    if form.validate_on_submit():
        name=form.name.data
        pup=Puppy(name)
        db.session.add(pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template("add.html",form=form)


@app.route('/delete',methods=['GET','POST'])

def del_pup():
    form=Delform()
    if form.validate_on_submit():
        id=form.id.data
        pup=Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for("list_pup"))
    return render_template("delete.html",form=form)

@app.route('/list')

def list_pup():
    puppies=Puppy.query.all()
    return render_template("list.html",puppies=puppies)


@app.route('/add_owner',methods=['GET','POST'])

def add_owner():
    form=Addownerform()
    if form.validate_on_submit():
        name=form.name.data

        puppy_id=form.puppy_id.data
        owner=Owner(name,puppy_id)
        db.session.add(owner)
        db.session.commit()
        return redirect(url_for("list_pup"))
    return render_template("addowner.html",form=form)



if __name__=='__main__':
    app.run(debug=True)
