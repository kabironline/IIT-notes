from database import db


class Student(db.Model):
    __table_name__ = 'students'
    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roll_number = db.Column(db.String(10), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50))
