from models import Course
from week_5 import *
from database import db


def add_course(course_id, course_code, course_name, course_description):
    course = Course(
        course_id=course_id,
        course_code=course_code,
        course_name=course_name,
        course_description=course_description
    )

    db.session.add(course)
    db.session.commit()
    return course


def get_course_by_code(course_code):
    course = Course.query.filter_by(course_code=course_code).first()
    return course


def init_courses_tables():
    session = db.session
    # select * from course
    count = session.query(Course).count()
    if count == 4:
        return
    else:
        # delete all rows from course
        session.query(Course).delete()
        session.commit()
        # insert 4 rows into course
        add_course(1, "CSE01", "MAD 1", "Mobile Application Development 1")
        add_course(2, "CSE02", "DBMS", "Database Management System")
        add_course(3, "CSE03", "PDSA",
                   "Programming, Data Structures and Algorithms using Python")
        add_course(4, "CSE04", "BDM", "Business Data Management")

        print("Course table initialized")
