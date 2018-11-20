from flask import Flask,render_template,redirect,url_for,Blueprint
from myproject import db
from myproject.owners.forms import Addownerform
from myproject.models import Owner

owner_blueprint=Blueprint('owners',__name__,template_folder='templates/owners')

@owner_blueprint.route('/add',methods=['GET','POST'])

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
