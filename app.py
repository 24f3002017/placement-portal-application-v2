from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager , create_access_token
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
    
    if user.role == "company":
        company = Company.query.filter_by(user_id=user.id).first()
        
        if company.approval_status != "approved":
            return jsonify({
                "message": "Company is waiting for admin approval"
            }), 403
    
    token = create_access_token(identity=user.id)
    
    return jsonify({
        "message": "Login successful",
        "token": token,
        "role": user.role
    }), 200
        
if __name__ == "__main__":
    app.run(debug=True)
    