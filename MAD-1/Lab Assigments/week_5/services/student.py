from models import Student
from database import db


def get_all_students():
    students = db.session.query(Student).all()
    return students


def get_student_by_id(student_id):
    return Student.query.filter_by(student_id=student_id).first()


def create_student(roll_number, first_name, last_name):
    if db.session.query(Student).filter_by(roll_number=roll_number).first():
        return None

    student = Student(
        roll_number=roll_number,
        first_name=first_name,
        last_name=last_name
    )
    db.session.add(student)
    db.session.commit()

    return student


def update_student(student_id, roll_number, first_name, last_name):
    student = Student.query.filter_by(student_id=student_id).first()
    student.roll_number = roll_number
    student.first_name = first_name
    student.last_name = last_name
    db.session.commit()
    return student


def delete_student(student_id):
    student = Student.query.filter_by(student_id=student_id).first()
    db.session.delete(student)
    db.session.commit()
    return student
