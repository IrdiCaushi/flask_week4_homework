from flask import Flask, jsonify, render_template
from blueprints.student_blueprint import student_bluep
from blueprints.course_blueprint import course_bluep
from blueprints.event_blueprint import event_bluep


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

    

app.register_blueprint(student_bluep, url_prefix='/v1/student')

app.register_blueprint(event_bluep, url_prefix='/v2/event')

app.register_blueprint(course_bluep, url_prefix='/v3/course')