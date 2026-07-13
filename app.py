from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager , create_access_token , jwt_required , get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Admin , User , Student , Company , JobPosition , Application , Placement
from datetime import datetime

ADMIN_EMAIL = "admin@gmail.com"
ADMIN_PASSWORD = "admin123"

app = Flask(__name__)

app.config["SECRET_KEY"] = "placement_portal_secret_key"
app.config["JWT_SECRET_KEY"] = "placement_portal_jwt_secret"

CORS(app)
jwt = JWTManager(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    if not User.query.filter_by(email=ADMIN_EMAIL).first():
        admin_user = User(
            email=ADMIN_EMAIL,
            password_hash=generate_password_hash(ADMIN_PASSWORD),
            role="admin"
        )
        db.session.add(admin_user)
        db.session.commit()

        admin = Admin(user_id=admin_user.id)
        db.session.add(admin)
        db.session.commit()

def check_user_status():

    user = User.query.get(get_jwt_identity())

    if user.status == "inactive":
        return jsonify({
            "message": "Your account has been deactivated."
        }), 403

    if user.status == "blacklisted":
        return jsonify({
            "message": "Your account has been blacklisted."
        }), 403

    return None

@app.route("/")
def home():
    return jsonify({
        "message": "Placement Portal API is running"
    }), 200

@app.route("/api/student/register", methods=["POST"])
def student_register():
    
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    roll_no = data.get("roll_no")
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    skills = data.get("skills")
    cgpa = data.get("cgpa")
    experience = data.get("experience")
    resume = data.get("resume")
    education = data.get("education")

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({"message": "Email already registered"}), 400
    
    try:
        hashed_password = generate_password_hash(password)
        
        new_user = User(
            email=email,
            password_hash=hashed_password,
            role="student"
        )
        db.session.add(new_user)
        db.session.flush()
        
        new_student = Student(
            user_id=new_user.id,
            roll_no=roll_no,
            first_name=first_name,
            last_name=last_name,
            skills=skills,
            cgpa=cgpa,
            experience=experience,
            resume=resume,
            education=education
        )
        db.session.add(new_student)
        db.session.commit()

        return jsonify({
            "message": "Student registered successfully"
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "message": "Registration failed",
        }), 500
    
@app.route("/api/company/register", methods=["POST"])
def company_register():
    
    data = request.get_json()
    
    email = data.get("email")
    password = data.get("password")
    name = data.get("name")
    hr_contact = data.get("hr_contact")
    website = data.get("website")
    industry = data.get("industry")

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({"message": "Email already registered"}), 400
    try:
        hashed_password = generate_password_hash(password)
        
        new_user = User(
            email=email,
            password_hash=hashed_password,
            role="company"
        ) 
        db.session.add(new_user)
        db.session.flush()
        
        new_company = Company(
            user_id=new_user.id,
            name=name,
            hr_contact=hr_contact,
            website=website,
            industry=industry,
            approval_status="pending"
        )
        db.session.add(new_company)
        db.session.commit()
        
        return jsonify({
            "message": "Company registered successfully"
        }), 201
    
    except Exception:
        db.session.rollback()
        return jsonify({
            "message": "Registration failed"
        }), 500
    
@app.route("/api/login", methods=["POST"])
def login():
    
    data = request.get_json()
    
    email = data.get("email")
    password = data.get("password")
    
    user = User.query.filter_by(email=email).first()
    
    if not user:
        return jsonify({
            "message": "User does not exist"
        }), 401

    if not check_password_hash(user.password_hash, password):
        return jsonify({
            "message": "Invalid email or password"
        }), 401
    if user.status == "inactive":
        return jsonify({
            "message": "Your account has been deactivated. Contact the administrator."
            }), 403
    
    if user.status == "blacklisted":
        return jsonify({
        "message": "Your account has been blacklisted."
        }), 403
    
    if user.role == "company":
        company = Company.query.filter_by(user_id=user.id).first()
        
        if company.approval_status != "approved":
            return jsonify({
                "message": "Company is waiting for admin approval"
            }), 403
    
    token = create_access_token(identity=str(user.id))
    
    return jsonify({
        "message": "Login successful",
        "token": token,
        "role": user.role
    }), 200

@app.route("/api/admin/dashboard", methods=["GET"])
@jwt_required()
def admin_dashboard():

    status = check_user_status()
    
    if status:
        return status

    total_students = Student.query.count()
    total_companies = Company.query.count()
    total_jobs = JobPosition.query.count()
    total_applications = Application.query.count()
    total_placements = Placement.query.count()

    return jsonify({
        "students": total_students,
        "companies": total_companies,
        "jobs": total_jobs,
        "applications": total_applications,
        "placements": total_placements
    }), 200

@app.route("/api/admin/companies", methods=["GET"])
@jwt_required()
def get_companies():

    status = check_user_status()
    
    if status:
        return status

    companies = Company.query.all()

    result = []

    for company in companies:

        result.append({
            "id": company.id,
            "name": company.name,
            "industry": company.industry,
            "website": company.website,
            "status": company.approval_status
        })

    return jsonify(result), 200

@app.route("/api/admin/company/<int:id>", methods=["GET"])
@jwt_required()
def get_company(id):

    status = check_user_status()
    
    if status:
        return status

    company = Company.query.get(id)

    if not company:
        return jsonify({
            "message": "Company not found"
        }), 404

    user = User.query.get(company.user_id)

    return jsonify({

        "id": company.id,
        "name": company.name,
        "email": user.email,
        "industry": company.industry,
        "website": company.website,
        "hr_contact": company.hr_contact,
        "approval_status": company.approval_status,
        "status":user.status

    }), 200

@app.route("/api/admin/pending-companies", methods=["GET"])
@jwt_required()
def pending_companies():

    status = check_user_status()
    
    if status:
        return status

    companies = Company.query.filter_by(
        approval_status="pending"
    ).all()

    result = []

    for company in companies:

        result.append({
            "id": company.id,
            "name": company.name,
            "industry": company.industry,
            "website": company.website,
            "hr_contact": company.hr_contact
        })
    return jsonify(result), 200

@app.route("/api/admin/company/<int:id>/approve", methods=["PUT"])
@jwt_required()
def approve_company(id):

    status = check_user_status()
    
    if status:
        return status
    
    company = Company.query.get_or_404(id)
    company.approval_status = "approved"
    db.session.commit()
    return jsonify({"message": "Company approved"}), 200

@app.route("/api/admin/company/<int:id>/reject", methods=["PUT"])
@jwt_required()
def reject_company(id):

    status = check_user_status()
    
    if status:
        return status
    
    company = Company.query.get_or_404(id)
    company.approval_status = "rejected"
    db.session.commit()
    return jsonify({"message": "Company rejected"}), 200

@app.route("/api/admin/company/<int:id>/activate", methods=["PUT"])
@jwt_required()
def activate_company(id):

    status = check_user_status()
    
    if status:
        return status

    company = Company.query.get_or_404(id)

    company.user.status = "active"

    db.session.commit()

    return jsonify({"message": "Company activated"}), 200

@app.route("/api/admin/company/<int:id>/deactivate", methods=["PUT"])
@jwt_required()
def deactivate_company(id):

    status = check_user_status()
    
    if status:
        return status

    company = Company.query.get_or_404(id)

    company.user.status = "inactive"

    db.session.commit()

    return jsonify({"message": "Company deactivated"}), 200

@app.route("/api/admin/company/<int:id>/blacklist", methods=["PUT"])
@jwt_required()
def blacklist_company(id):

    status = check_user_status()
    
    if status:
        return status

    company = Company.query.get_or_404(id)

    company.user.status = "blacklisted"

    db.session.commit()

    return jsonify({"message": "Company blacklisted"}), 200

@app.route("/api/admin/company/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_company(id):

    status = check_user_status()
    
    if status:
        return status

    company = Company.query.get_or_404(id)

    if company.user.status == "blacklisted":
        return jsonify({"message": "Blacklisted company cannot be deleted"}), 403

    user = company.user

    db.session.delete(company)
    db.session.delete(user)

    db.session.commit()

    return jsonify({"message": "Company deleted"}), 200

@app.route("/api/admin/students", methods=["GET"])
@jwt_required()
def get_students():

    status = check_user_status()
    
    if status:
        return status

    students = Student.query.all()

    result = []

    for student in students:

        user = User.query.get(student.user_id)

        result.append({
            "id": student.id,
            "name": student.first_name + " " + student.last_name,
            "roll_no": student.roll_no,
            "email": user.email,
            "status": user.status
        })

    return jsonify(result), 200

@app.route("/api/admin/student/<int:id>", methods=["GET"])
@jwt_required()
def get_student(id):

    status = check_user_status()
    
    if status:
        return status

    student = Student.query.get_or_404(id)
    user = User.query.get(student.user_id)

    return jsonify({

        "id": student.id,
        "first_name": student.first_name,
        "last_name": student.last_name,
        "roll_no": student.roll_no,
        "email": user.email,
        "cgpa": student.cgpa,
        "skills": student.skills,
        "experience": student.experience,
        "education": student.education,
        "resume": student.resume,
        "status": user.status

    }), 200

@app.route("/api/admin/student/<int:id>/activate", methods=["PUT"])
@jwt_required()
def activate_student(id):

    status = check_user_status()
    
    if status:
        return status

    student = Student.query.get_or_404(id)

    user = User.query.get(student.user_id)

    user.status = "active"

    db.session.commit()

    return jsonify({
        "message": "Student activated"
    }), 200

@app.route("/api/admin/student/<int:id>/deactivate", methods=["PUT"])
@jwt_required()
def deactivate_student(id):

    status = check_user_status()
    
    if status:
        return status

    student = Student.query.get_or_404(id)

    user = User.query.get(student.user_id)

    user.status = "inactive"

    db.session.commit()

    return jsonify({
        "message": "Student deactivated"
    }), 200

@app.route("/api/admin/student/<int:id>/blacklist", methods=["PUT"])
@jwt_required()
def blacklist_student(id):

    status = check_user_status()
    
    if status:
        return status

    student = Student.query.get_or_404(id)

    user = User.query.get(student.user_id)

    user.status = "blacklisted"

    db.session.commit()

    return jsonify({
        "message": "Student blacklisted"
    }), 200

@app.route("/api/admin/student/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_student(id):

    status = check_user_status()
    
    if status:
        return status

    student = Student.query.get_or_404(id)

    user = User.query.get(student.user_id)

    if user.status == "blacklisted":

        return jsonify({
            "message": "Blacklisted students cannot be deleted."
        }), 403

    db.session.delete(student)
    db.session.delete(user)

    db.session.commit()

    return jsonify({
        "message": "Student deleted successfully."
    }), 200

@app.route("/api/admin/jobs", methods=["GET"])
@jwt_required()
def get_jobs():

    status = check_user_status()
    
    if status:
        return status

    jobs = JobPosition.query.all()

    result = []

    for job in jobs:

        company = Company.query.get(job.company_id)

        result.append({

            "id": job.id,
            "company": company.name,
            "title": job.title,
            "deadline": job.deadline,
            "salary": job.salary,
            "approval_status": job.job_approval_status,
            "status": job.current_status

        })

    return jsonify(result), 200

@app.route("/api/admin/job/<int:id>", methods=["GET"])
@jwt_required()
def get_job(id):

    status = check_user_status()
    
    if status:
        return status

    job = JobPosition.query.get_or_404(id)

    company = Company.query.get(job.company_id)

    return jsonify({

        "id": job.id,
        "company": company.name,
        "title": job.title,
        "description": job.description,
        "eligibility": job.eligibility,
        "salary": job.salary,
        "skills_req": job.skills_req,
        "exp_req": job.exp_req,
        "deadline": job.deadline,
        "approval_status": job.job_approval_status,
        "status": job.current_status

    }), 200

@app.route("/api/admin/job/<int:id>/approve", methods=["PUT"])
@jwt_required()
def approve_job(id):

    status = check_user_status()
    
    if status:
        return status

    job = JobPosition.query.get_or_404(id)

    job.job_approval_status = "approved"
    job.current_status = "active"

    db.session.commit()

    return jsonify({
        "message": "Job approved successfully."
    }), 200

@app.route("/api/admin/job/<int:id>/reject", methods=["PUT"])
@jwt_required()
def reject_job(id):

    status = check_user_status()
    
    if status:
        return status

    job = JobPosition.query.get_or_404(id)

    job.job_approval_status = "rejected"
    job.current_status = "inactive"

    db.session.commit()

    return jsonify({
        "message": "Job rejected."
    }), 200

@app.route("/api/admin/job/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_job(id):

    status = check_user_status()
    
    if status:
        return status

    job = JobPosition.query.get_or_404(id)

    db.session.delete(job)

    db.session.commit()

    return jsonify({
        "message": "Job deleted successfully."
    }), 200

@app.route("/api/admin/applications", methods=["GET"])
@jwt_required()
def get_all_applications():

    status = check_user_status()
    
    if status:
        return status

    applications = Application.query.all()

    result = []

    for application in applications:

        student = Student.query.get(application.student_id)
        company = Company.query.get(application.company_id)
        job = JobPosition.query.get(application.job_position_id)

        result.append({

            "id": application.id,
            "student": student.first_name + " " + student.last_name,
            "company": company.name,
            "job": job.title,
            "date": application.application_date.strftime("%d-%m-%Y"),
            "status": application.status

        })

    return jsonify(result), 200

@app.route("/api/admin/placements", methods=["GET"])
@jwt_required()
def get_all_placements():

    status = check_user_status()
    
    if status:
        return status

    placements = Placement.query.all()

    result = []

    for placement in placements:

        student = Student.query.get(placement.student_id)
        company = Company.query.get(placement.company_id)
        job = JobPosition.query.get(placement.job_position_id)

        result.append({

            "id": placement.id,
            "student": student.first_name + " " + student.last_name,
            "company": company.name,
            "job": job.title,
            "date": placement.placement_date.strftime("%d-%m-%Y")

        })

    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True)
    