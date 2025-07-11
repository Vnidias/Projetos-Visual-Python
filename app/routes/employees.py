from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models import User
from app.extensions import db
from datetime import datetime

employees = Blueprint('employees', __name__)

@employees.route('/employees')
@login_required
def index():
    all_users = User.query.all()
    return render_template('employees.html', users=all_users)

@employees.route('/employees/add', methods=['POST'])
@login_required
def add():
    username = request.form['username']
    email = request.form['email']
    function = request.form['function']
    permission = request.form['permission']
    password = request.form['password']

    new_user = User(
        username=username,
        email=email,
        function=function,
        permission=permission,
        password=password
    )

    db.session.add(new_user)
    db.session.commit()
    flash("✅ User added successfully!", "success")
    return redirect(url_for('employees.index'))

@employees.route('/employees/delete/<int:user_id>', methods=['POST'])
@login_required
def delete(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("🗑️ User deleted!", "info")
    return redirect(url_for('employees.index'))
