from flask import Blueprint, render_template
from flask_login import login_required
from app.models import Attendance
from app.extensions import db
from datetime import datetime
from sqlalchemy import func

reports = Blueprint('reports', __name__)

@reports.route('/monthly_report')
@login_required
def view():
    current_month = datetime.now().month
    current_year = datetime.now().year

    report = db.session.query(
        Attendance.employee_name,
        func.sum(Attendance.hours_worked).label('total_hours')
    ).filter(
        func.extract('month', Attendance.date_worked) == current_month,
        func.extract('year', Attendance.date_worked) == current_year
    ).group_by(Attendance.employee_name).all()

    return render_template('report.html', report=report)
