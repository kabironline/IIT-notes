import csv
import sys
import matplotlib.pyplot as plt
import pyhtml as h
import jinja2 as j2

html_template = j2.Template("""
<!DOCTYPE html>
<html>
    <head>
        <title> {{ title }} </title>
    </head>
    <body>
        <h1> {{ heading }} </h1>
        {{ body }}
    </body>
</html>
""")

wrong_id_template = "<p>Something went wrong</p>"


def generate_student_table(marks):
    total_marks = 0
    for i in marks:
        total_marks += int(i[2])
    template = j2.Template("""
    <table style= "text-align: center; border: 1px solid black; border-collapse: collapse;">
        <tr>
            <th style= "border: 1px solid black;padding= 2px">Subject id</th>
            <th style= "border: 1px solid black;padding= 2px">Course id</th>
            <th style= "border: 1px solid black;padding= 2px">Marks</th>
        </tr>
        {% for i in marks %}
        <tr>
            <td style= "border: 1px solid black;">{{ i[0] }}</td>
            <td style= "border: 1px solid black;">{{ i[1] }}</td>
            <td style= "border: 1px solid black;">{{ i[2] }}</td>
        </tr>
        {% endfor %}
        <tr>
            <td style= "border: 1px solid black;" colspan="2">Total Marks</td>
            <td style= "border: 1px solid black;">{{ total_marks }}</td>
        </tr>
    </table>
    """)

    return template.render(marks=marks, total_marks=total_marks)


def generate_course_table(marks):
    total_marks = 0
    max_marks = 0
    for i in marks:
        total_marks += int(i[2])
        max_marks = max(max_marks, int(i[2]))
    average = total_marks / len(marks)
    template = j2.Template("""
    <table style= "text-align: center; border: 1px solid black; border-collapse: collapse;">
        <tr>
            <th style= "border: 1px solid black;padding= 2px">Average Marks</th>
            <th style= "border: 1px solid black;padding= 2px">Total Marks</th>
        </tr>
        <tr>
            <td style= "border: 1px solid black;">{{ average}}</td>
            <td style= "border: 1px solid black;">{{ max_m}}</td>
        </tr>
    </table>
    <img src="histogram.png" alt="histogram">
    """)

    return template.render(average=average, max_m=max_marks)


def generate_graph(marks):
    # Generate a frequency distribution of the marks
    marks_list = []
    for i in marks:
        marks_list.append(int(i[2]))
    plt.hist(marks_list, bins=10)
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    plt.savefig('histogram.png')
    plt.close()
    return h.img(src='histogram.png')


# read the arguments from the command line and store them in variables
# the first argument is the name of the script, so we ignore it
script_name, arg, id = sys.argv


def generate(arg, id):
    file_name = 'data.csv'
    # open the csv file
    if arg == '-s':
        data = []
        # reading the rows with the marks of the roll number
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == id:
                    data.append(row)
        if len(data) == 0:
            return "Something Went Wrong", "Wrong Inputs", wrong_id_template
        # putting the data in the html template
        return "Student Details", "Student Details", generate_student_table(data)
    elif arg == '-c':
        data = []
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1].strip() == id:
                    data.append(row)
        if len(data) == 0:
            return "Something Went Wrong", "Wrong Inputs", wrong_id_template
        generate_graph(data)
        return "Course Data", "Course Details", generate_course_table(data)
    else:
        return "Something Went Wrong", "Wrong Inputs", wrong_id_template


title, heading, body = (generate(arg, id))
# write the html file
with open('ouput.html', 'w') as file:
    file.write(html_template.render(title=title, heading=heading, body=body))
