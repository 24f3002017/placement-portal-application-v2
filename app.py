from flask import Flask
from models import db, Admin , User , Student , Company , Drive , Application , Placement
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    if not User.query.filter_by(email="admin@gmail.com").first():
        admin_user = User(
            email="admin@gmail.com",
            password_hash="admin123",
            role="admin"
        )
        db.session.add(admin_user)
        db.session.commit()

@app.route("/")
def home():
    return "Placement Portal Application V2"

if __name__ == "__main__":
    app.run(debug=True)
    