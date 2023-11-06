from models import Student
from services import *
from flask import Flask, render_template, request, redirect, url_for
from database import db
import os

app = Flask(__name__)
current_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
db.init_app(app)


@app.route('/')
def index():
    # Get all students

    students = db.session.query(Student).all()
    return render_template('home.html', students=students, length=len(students))


@app.route('/student/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        roll_number = request.form.get('roll')
        first_name = request.form.get('f_name')
        last_name = request.form.get('l_name')
        courses = request.form.getlist('courses')
        student = create_student(roll_number, first_name, last_name)

        if student is None:
            return render_template('error.html', message="Student already exists. Please use different Roll Number!")

        enrollments = create_enrollment(student.student_id, courses)
        return redirect(url_for('index'))
    else:
        return render_template('create.html')


@app.route('/student/<int:student_id>/delete', methods=['GET'])
def delete(student_id):
    delete_student(student_id)
    delete_enrollment(student_id)
    return redirect(url_for('index'))


@app.route('/student/<int:student_id>', methods=['GET'])
def profile(student_id):
    student = get_student_by_id(student_id)
    courses = [get_course_by_code(enrollment.course_id)
               for enrollment in get_enrollment_by_student_id(student_id)]
    return render_template('profile.html', student=student, courses=courses)


@app.route('/student/<int:student_id>/update', methods=['GET', 'POST'])
def update(student_id):
    student = get_student_by_id(student_id)
    if request.method == 'POST':
        roll_number = request.form.get('roll')
        first_name = request.form.get('f_name')
        last_name = request.form.get('l_name')
        courses = request.form.getlist('courses')
        delete_enrollment(student.student_id)
        enrollments = create_enrollment(student.student_id, courses)
        student = update_student(
            student_id, student.roll_number, first_name, last_name)
        return redirect(url_for('index'))
    else:
        return render_template('update.html', student=student)


app.run(debug=True)
