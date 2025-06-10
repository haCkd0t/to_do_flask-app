from flask import url_for,redirect,Blueprint,request,session,render_template,flash
from app.models.models import Tasks,Users
from app import db

tasks_bp = Blueprint('tasks',__name__)

@tasks_bp.route("/view_tasks")
def view_tasks():
    if 'user' in session:
        user = session['user']
        f = Users.query.filter_by(name=user).first()
        id = f.id
        tasks = Tasks.query.filter_by(user_id=id)
        return render_template("tasks.html",tasks=tasks)
    else:
        flash("LOGIN FIRST")
        return redirect(url_for("auth.login"))

@tasks_bp.route("/add-task",methods=['POST'])
def add_task():
    if 'user' in session:
        title = request.form.get('title')
        status = request.form.get('status')
        name = session['user']
        user = Users.query.filter_by(name=name).first()
        id = user.id
        new_task = Tasks(title=title,status=status,user_id=id)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('tasks.view_tasks'))
    return redirect(url_for('tasks.view_tasks'))


@tasks_bp.route("/delete/<int:id>",methods=['POST'])
def delete(id):
    task = Tasks.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route("/update",methods=['POST'])
def update():
    id = request.args.get('id',type=int)
    status = request.args.get('t_status')
    task = Tasks.query.get_or_404(id)
    if task.status == "Pending":
        task.status = "In_progress"
    elif task.status == "In_progress":
        task.status = "Done"
    elif task.status == "Done":
        task.status = "Pending"
    db.session.commit()
    return redirect(url_for('tasks.view_tasks'))