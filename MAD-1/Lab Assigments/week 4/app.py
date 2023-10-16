import csv
import matplotlib.pyplot as plt
import flask

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'POST':
        arg = flask.request.form.get('type')
        roll = flask.request.form.get('roll')
        if not roll or arg not in ('student', 'course'):
            return flask.render_template('error.html')

        data = read_csv_data("data.csv")

        if arg == 'student':
            student_data = find_student_data(data, roll)
            if not student_data:
                return flask.render_template('error.html')
            marks, total = generate_student_table(student_data)
            return flask.render_template('student.html', heading='Student Details', title='Student Details', type='student', marks=marks, total=total)

        if arg == 'course':
            course_data = find_course_data(data, roll)
            if not course_data:
                return flask.render_template('error.html')
            max_marks, average = generate_course_table(course_data)
            generate_graph(course_data)
            return flask.render_template('course.html', title='Course Details', heading='Course Data', max_m=max_marks, average=average)

    return flask.render_template('index.html')


def read_csv_data(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


def find_student_data(data, roll):
    return [row for row in data if row[0] == str(roll)]


def find_course_data(data, roll):
    return [row for row in data if row[1].strip() == str(roll)]


def generate_student_table(marks):
    total_marks = sum(int(row[2]) for row in marks)
    return marks, total_marks


def generate_course_table(marks):
    total_marks = sum(int(row[2]) for row in marks)
    max_marks = max(int(row[2]) for row in marks)
    average = total_marks / len(marks)
    return max_marks, average


def generate_graph(marks):
    marks_list = [int(row[2]) for row in marks]
    plt.hist(marks_list, bins=10)
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    plt.savefig('static/histogram.png')
    plt.close()


app.run(debug=True)
