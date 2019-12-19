from flask import Flask, render_template, request
app = Flask(__name__)

import sqlite3
from sqlite3 import Error


con = sqlite3.connect('toy.db', check_same_thread=False)
cursorObj = con.cursor()

@app.route('/courses', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return getCourses()

    if request.method == "POST":
        return commitCourse()
    
def getCourses():
    cursorObj.execute('select * from courses')
    rows = cursorObj.fetchall()
    return render_template('index.html', result=rows)

@app.route('/createCourse')
def createCourse():
    return render_template('create_course.html')

def commitCourse():
    print(request.method)
    
    q = "insert into Courses values(" \
    + str(request.form['courseId']) + ",'" \
    + str(request.form['courseName']) + "','" \
    + str(request.form['department']) + "')"
    
    print(q)
    cursorObj.execute(q)
    con.commit()
    cursorObj.execute('select * from courses')
    rows = cursorObj.fetchall()
    return render_template('index.html', result=rows)

if __name__ == "__main__":
    app.run(debug=True)