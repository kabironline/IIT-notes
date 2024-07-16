from database import db


class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    enrollment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey(
        'student.student_id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey(
        'course.course_id'), nullable=False)
