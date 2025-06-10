from flask import url_for,redirect,request,render_template,session,Blueprint,flash
from app.models.models import Users

auth_bp = Blueprint('auth',__name__)

@auth_bp.route("/",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        user = Users.query.filter_by(name=name).first()
        if user and user.password == password:
            flash(f"hello {name} Nice to have you")
            session['user'] = name
        else:
            return "Invalid-Creds"
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.pop('user', None)
    return "Logout Successfully"