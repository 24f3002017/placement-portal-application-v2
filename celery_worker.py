from celery import Celery
from app import app, mail, ADMIN_EMAIL
from flask_mail import Message
import csv
import os
from models import Student, Company, Application, JobPosition, Placement
from sqlalchemy import func
from datetime import datetime , date , timedelta
from celery.schedules import crontab

celery = Celery(
    "placement_portal",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery.conf.update(
    result_expires=3600,
    timezone="Asia/Kolkata",
    enable_utc=False
)

celery.conf.beat_schedule = {

    "daily-deadline-reminder": {

        "task": "celery_worker.application_deadline_reminder",

        "schedule": crontab(

            hour=22,

            minute=43

        )

    },

    "daily-interview-reminder": {

        "task": "celery_worker.daily_interview_reminder",

        "schedule": crontab(

            hour=22,

            minute=44

        )

    },

    "monthly-placement-report": {

        "task": "celery_worker.monthly_report",

        "schedule": crontab(

            # day_of_month=1,

            hour=22,

            minute=45

        )

    }

}

@celery.task
def add(x, y):
    return x + y

@celery.task
def send_interview_email(
    student_email,
    student_name,
    company_name,
    job_title,
    interview_date,
    interview_time,
    interview_mode,
    interview_location
):

    with app.app_context():

        msg = Message(
            subject="Interview Scheduled - Placement Portal",
            recipients=[student_email]
        )

        msg.body = f"""
Hello {student_name},

Your interview has been scheduled.

Company: {company_name}

Job Position: {job_title}

Date: {interview_date}

Time: {interview_time}

Mode: {interview_mode}

Location / Meeting Link:
{interview_location}

Best of luck!

Regards,
Placement Portal
"""

        mail.send(msg)

@celery.task
def export_student_csv(student_id):

    with app.app_context():

        student = Student.query.get(student_id)

        if not student:
            return

        export_folder = os.path.join(app.config["UPLOAD_FOLDER"], "exports")
        os.makedirs(export_folder, exist_ok=True)

        filename = f"student_{student.id}_applications.csv"
        filepath = os.path.join(export_folder, filename)

        applications = Application.query.filter_by(
            student_id=student.id
        ).all()

        with open(filepath, "w", newline="", encoding="utf-8") as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow([
                "Company",
                "Job Position",
                "Application Date",
                "Status",
                "Interview Date",
                "Interview Time",
                "Interview Mode",
                "Package"
            ])

            for application in applications:

                company = Company.query.get(application.company_id)

                job = JobPosition.query.get(application.job_position_id)

                placement = Placement.query.filter_by(
                    application_id=application.id
                ).first()

                writer.writerow([
                    company.name if company else "",
                    job.title if job else "",
                    application.application_date.strftime("%d-%m-%Y"),
                    application.status,
                    application.interview_date if application.interview_date else "",
                    application.interview_time if application.interview_time else "",
                    application.interview_mode if application.interview_mode else "",
                    placement.package if placement else ""
                ])

        msg = Message(
            subject="CSV Export Completed",
            recipients=[student.user.email]
        )

        msg.body = f"""
Hello {student.first_name},

Your application history has been exported successfully.

The CSV file is attached with this email.

Regards,
Placement Portal
"""

        with open(filepath, "rb") as f:
            msg.attach(
                filename,
                "text/csv",
                f.read()
            )

        mail.send(msg)

@celery.task
def export_company_csv(company_id):

    with app.app_context():

        company = Company.query.get(company_id)

        if not company:
            return

        applications = Application.query.filter_by(
            company_id=company.id
        ).all()

        export_folder = os.path.join(
            app.config["UPLOAD_FOLDER"],
            "exports"
        )
        
        os.makedirs(export_folder, exist_ok=True)
        
        filename = f"company_{company.id}_applications.csv"
        
        filepath = os.path.join(
            export_folder,
            filename
        )
        
        with open(filepath, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Student",
                "Roll Number",
                "Job Position",
                "Application Date",
                "Status",
                "Interview Date",
                "Interview Time",
                "Interview Mode",
                "Package"
            ])

            for application in applications:

                student = Student.query.get(
                    application.student_id
                )

                job = JobPosition.query.get(
                    application.job_position_id
                )

                placement = Placement.query.filter_by(
                    application_id=application.id
                ).first()

                writer.writerow([

                    student.first_name + " " + student.last_name,

                    student.roll_no,

                    job.title,

                    application.application_date.strftime("%d-%m-%Y"),

                    application.status,

                    application.interview_date
                    if application.interview_date
                    else "",

                    application.interview_time
                    if application.interview_time
                    else "",

                    application.interview_mode
                    if application.interview_mode
                    else "",

                    placement.package
                    if placement
                    else ""

                ])

        msg = Message(

            subject="CSV Export Completed",

            recipients=[company.user.email]

        )

        msg.body = f"""
Hello,

Your company application history has been exported successfully.

The CSV file is attached with this email.

Regards,
Placement Portal
"""

        with open(filepath, "rb") as f:
            
            msg.attach(
                filename,
                "text/csv",
                f.read()
            )

        mail.send(msg)

        os.remove(filepath)

@celery.task
def monthly_report():

    with app.app_context():

        companies = Company.query.all()

        for company in companies:

            total_jobs = JobPosition.query.filter_by(
                company_id=company.id
            ).count()

            total_applications = Application.query.filter_by(
                company_id=company.id
            ).count()

            shortlisted = Application.query.filter_by(
                company_id=company.id,
                status="shortlisted"
            ).count()

            selected = Application.query.filter_by(
                company_id=company.id,
                status="selected"
            ).count()

            rejected = Application.query.filter_by(
                company_id=company.id,
                status="rejected"
            ).count()

            html = f"""
            <h2>Placement Portal - Monthly Company Report</h2>

            <p>Hello <b>{company.name}</b>,</p>

            <p>Here is your monthly placement report.</p>

            <table border="1" cellpadding="8" cellspacing="0">

                <tr>
                    <th>Total Job Postings</th>
                    <td>{total_jobs}</td>
                </tr>

                <tr>
                    <th>Total Applications</th>
                    <td>{total_applications}</td>
                </tr>

                <tr>
                    <th>Shortlisted</th>
                    <td>{shortlisted}</td>
                </tr>

                <tr>
                    <th>Selected</th>
                    <td>{selected}</td>
                </tr>

                <tr>
                    <th>Rejected</th>
                    <td>{rejected}</td>
                </tr>

            </table>

            <br>

            <p>
            This is an automated monthly report generated by the Placement Portal.
            </p>

            <p>
            Regards,<br>
            Placement Portal
            </p>
            """

            msg = Message(
                subject="Monthly Placement Report",
                recipients=[company.user.email]
            )

            msg.html = html

            mail.send(msg)

        total_students = Student.query.count()

        total_companies = Company.query.count()

        total_jobs = JobPosition.query.count()

        total_applications = Application.query.count()

        total_placements = Placement.query.count()

        shortlisted = Application.query.filter_by(
            status="shortlisted"
        ).count()

        selected = Application.query.filter_by(
            status="selected"
        ).count()

        rejected = Application.query.filter_by(
            status="rejected"
        ).count()

        admin_html = f"""
        <h2>Placement Portal - Monthly Admin Report</h2>

        <p>Hello <b>Admin</b>,</p>

        <p>Here is the monthly portal activity report.</p>

        <table border="1" cellpadding="8" cellspacing="0">

            <tr>
                <th>Total Students</th>
                <td>{total_students}</td>
            </tr>

            <tr>
                <th>Total Companies</th>
                <td>{total_companies}</td>
            </tr>

            <tr>
                <th>Total Job Postings</th>
                <td>{total_jobs}</td>
            </tr>

            <tr>
                <th>Total Applications</th>
                <td>{total_applications}</td>
            </tr>

            <tr>
                <th>Total Placements</th>
                <td>{total_placements}</td>
            </tr>

            <tr>
                <th>Shortlisted</th>
                <td>{shortlisted}</td>
            </tr>

            <tr>
                <th>Selected</th>
                <td>{selected}</td>
            </tr>

            <tr>
                <th>Rejected</th>
                <td>{rejected}</td>
            </tr>

        </table>

        <br>

        <p>
        This is an automated monthly report generated by the Placement Portal.
        </p>

        <p>
        Regards,<br>
        Placement Portal
        </p>
        """

        admin_msg = Message(
            subject="Monthly Placement Portal Report",
            recipients=[ADMIN_EMAIL]
        )

        admin_msg.html = admin_html

        mail.send(admin_msg)            

@celery.task
def daily_interview_reminder():

    with app.app_context():

        tomorrow = date.today() + timedelta(days=1)

        applications = Application.query.filter_by(
            interview_date=tomorrow
        ).all() 

        # applications = Application.query.all()

        for application in applications:

            student = Student.query.get(application.student_id)

            company = Company.query.get(application.company_id)

            job = JobPosition.query.get(application.job_position_id)

            msg = Message(

                subject="Interview Reminder",

                recipients=[student.user.email]

            )

            msg.body = f"""
Hello {student.first_name},

This is a reminder that you have an interview tomorrow.

Company : {company.name}

Job Position : {job.title}

Date : {application.interview_date}

Time : {application.interview_time}

Mode : {application.interview_mode}

Location : {application.interview_location}

Best of luck!

Placement Portal
"""

            mail.send(msg)

@celery.task
def application_deadline_reminder():

    with app.app_context():

        tomorrow = date.today() + timedelta(days=1)

        jobs = JobPosition.query.filter_by(
            current_status="active",
            job_approval_status="approved",
            deadline=tomorrow
        ).all()

        # jobs = JobPosition.query.all()

        students = Student.query.all()

        for job in jobs:

            company = Company.query.get(job.company_id)

            for student in students:

                existing = Application.query.filter_by(
                    student_id=student.id,
                    job_position_id=job.id
                ).first()

                if existing:
                    continue

                msg = Message(

                    subject="Placement Drive Deadline Reminder",

                    recipients=[student.user.email]

                )

                msg.body = f"""
Hello {student.first_name},

This is a reminder that the following placement drive closes tomorrow.

Company : {company.name}

Job Title : {job.title}

Application Deadline : {job.deadline}

Apply before the deadline if you are eligible.

Regards,
Placement Portal
"""

                mail.send(msg)