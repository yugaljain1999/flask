from flask import Flask,render_template,redirect,url_for,Blueprint
from myproject import db
from myproject.models import Puppy
from myproject.puppies.forms import Addform,Delform

puppies_blueprint=Blueprint('puppies',__name__,template_folder='templates/puppies')

@puppies_blueprint.route('/add',methods=['GET','POST'])
def add_pup():
    form=Addform()
    if form.validate_on_submit():
        name=form.name.data
        pup=Puppy(name)
        db.session.add(pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template("add.html",form=form)





@puppies_blueprint.route('/delete',methods=['GET','POST'])
def del_pup():
    form=Delform()
    if form.validate_on_submit():
        id=form.id.data
        pup=Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for("list_pup"))
    return render_template("delete.html",form=form)

@puppies_blueprint.route('/list')

def list_pup():
    puppies=Puppy.query.all()
    return render_template("list.html",puppies=puppies)
