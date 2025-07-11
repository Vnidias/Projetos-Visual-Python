from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime, timedelta
from app.models import Attendance
from app.extensions import db
import calendar

attendance = Blueprint('attendance', __name__)

@attendance.route('/attendance', methods=['GET', 'POST'])
@login_required
def view():
    week_start_str = request.args.get('week_start')
    if not week_start_str:
        today = datetime.today()
        start_of_week = today - timedelta(days=today.weekday())
    else:
        start_of_week = datetime.strptime(week_start_str, '%Y-%m-%d')

    dates = [start_of_week + timedelta(days=i) for i in range(5)]
    formatted_dates = [d.strftime('%a<br><small>%b %d</small>') for d in dates]
    date_strings = [d.strftime('%Y-%m-%d') for d in dates]

    return render_template('attendance.html', dates=formatted_dates, date_strings=date_strings, week_start=start_of_week.strftime('%Y-%m-%d'))

@attendance.route('/save_attendance', methods=['POST'])
@login_required
def save():
    employee_name = current_user.username
    for key, value in request.form.items():
        try:
            date_worked = datetime.strptime(key, '%Y-%m-%d').date()
            hours_worked = float(value)
            new_entry = Attendance(employee_name=employee_name, date_worked=date_worked, hours_worked=hours_worked)
            db.session.add(new_entry)
        except Exception as e:
            print("Error:", e)
    db.session.commit()
    flash("✅ Hours saved successfully!", "success")
    return redirect(url_for('attendance.view'))
