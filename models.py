from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    email = db.Column(db.String(100) , unique = True , nullable = False)
    password_hash = db.Column(db.String(200) , nullable = False)
    role = db.Column(db.String(20) , nullable = False)
    status = db.Column(db.String(15), nullable=False, default='active')

class Admin(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    user_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable = False)

    user = db.relationship('User')

class Student(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    user_id = db.Column(db.Integer , db.ForeignKey('user.id') , unique = True , nullable = False)
    roll_no = db.Column(db.String(50) , nullable = False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    skills = db.Column(db.String(200) , nullable = False)
    cgpa = db.Column(db.Float , nullable = False)
    experience = db.Column(db.Integer , nullable = False)
    resume = db.Column(db.String(200) , nullable = False)
    education = db.Column(db.String(100) , nullable = False)

    user = db.relationship('User')

    applications = db.relationship('Application',
                                   backref='student',
                                   cascade="all, delete")
    
    placements = db.relationship('Placement',
                                 backref='student',
                                 cascade="all, delete")
    
class Company(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    user_id = db.Column(db.Integer , db.ForeignKey('user.id') , unique = True , nullable = False)
    name = db.Column(db.String(100) , nullable = False)
    hr_contact = db.Column(db.String(100))
    website = db.Column(db.String(200))
    approval_status = db.Column(db.String(15) , nullable = False , default = 'pending')
    industry = db.Column(db.String(100) , nullable = False)

    user = db.relationship('User')

    job_positions = db.relationship('JobPosition',
                             backref='company',
                             cascade="all, delete")
    
    applications = db.relationship('Application',
                                   backref='company',
                                   cascade="all, delete")
    
    placements = db.relationship('Placement',
                                 backref='company',
                                 cascade="all, delete")
    
class JobPosition(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    company_id = db.Column(db.Integer , db.ForeignKey('company.id') , nullable = False)
    title = db.Column(db.String(50) , nullable = False)
    description = db.Column(db.Text)
    eligibility = db.Column(db.String(50))
    deadline = db.Column(db.Date)
    salary = db.Column(db.Integer)
    skills_req = db.Column(db.String(200))
    exp_req = db.Column(db.Integer)
    job_approval_status = db.Column(db.String(15) , nullable = False , default = 'pending')
    current_status = db.Column(db.String(15) , nullable = False , default = 'inactive')

    applications = db.relationship('Application',
                                   backref='job_position',
                                   cascade="all, delete")
    
    placements = db.relationship('Placement',
                                 backref='job_position',
                                 cascade="all, delete")

class Application(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    student_id = db.Column(db.Integer , db.ForeignKey('student.id') , nullable = False)
    company_id = db.Column(db.Integer , db.ForeignKey('company.id') , nullable = False)
    job_position_id = db.Column(db.Integer , db.ForeignKey('job_position.id'), nullable = False)
    application_date = db.Column(db.DateTime , default = datetime.utcnow)
    status = db.Column(db.String(15) , nullable = False , default = 'applied')

class Placement(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    application_id = db.Column(db.Integer, db.ForeignKey('application.id') , nullable = False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id') , nullable = False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id') , nullable = False)
    job_position_id = db.Column(db.Integer, db.ForeignKey('job_position.id') , nullable = False)
    placement_date = db.Column(db.Date, default=lambda: datetime.utcnow().date())

    application = db.relationship('Application')