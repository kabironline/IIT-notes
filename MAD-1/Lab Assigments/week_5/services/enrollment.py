from models import Enrollment
from database import db

course_map = {'course_1': 'CSE01', 'course_2': 'CSE02',
              'course_3': 'CSE03', 'course_4': 'CSE04'}


def create_enrollment(student_id, courses):
    enrollments = []
    for course in courses:
        enrollment = Enrollment(
            student_id=student_id,
            course_id=course_map[course]
        )
        enrollments.append(enrollment)
        db.session.add(enrollment)
    db.session.commit()
    return enrollments


def get_enrollment_by_student_id(student_id):
    enrollments = Enrollment.query.filter_by(student_id=student_id).all()
    return enrollments


def delete_enrollment(student_id):
    enrollments = Enrollment.query.filter_by(student_id=student_id).all()
    for enrollment in enrollments:
        db.session.delete(enrollment)
    db.session.commit()
    return enrollments
