from flask import render_template

@app.route('/lessons')
def lessons_list():
    return render_template('lessons_list.html')

@app.route('/lesson/1')
def lesson1_variables():
    return render_template('lesson1_variables.html')

@app.route('/lesson/2')
def lesson2_conditions():
    return render_template('lesson2_conditions.html')

@app.route('/lesson/3')
def lesson3_loops():
    return render_template('lesson3_loops.html')