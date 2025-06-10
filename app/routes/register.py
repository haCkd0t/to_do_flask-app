from flask import url_for,redirect,request,render_template, Blueprint,flash
from app import db
from app.models.models import Users,Tasks

reg_bp = Blueprint('register',__name__)

@reg_bp.route("/register",methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        ex_user = Users.query.filter_by(name=name).first()
        if ex_user:
            flash("User Already Exists")
            return redirect(url_for('register.register'))
        else:
            new = Users(name=name,password=password)
            db.session.add(new)
            db.session.commit()
            flash(f"User Added successfully")
            return redirect(url_for('register.register'))
    return render_template("register.html")
