from flask import Flask, render_template
app = Flask(__name__)

import sqlite3
from sqlite3 import Error


con = sqlite3.connect('toy.db', check_same_thread=False)
cursorObj = con.cursor()

@app.route('/index')
def index():
    cursorObj.execute('select * from courses')
    rows = cursorObj.fetchall()
    # for row in rows:
        # print(row)
        # print(row[0])
    #return render_template('index.html', var1=str(row[0]))
    return render_template('index.html', result=rows)



if __name__ == "__main__":
    app.run(debug=True)