import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    data = []
    with open("data/quiz.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("index.html", quiz_data=data)
    
@app.route('/africa_quiz')
def africa():
    return render_template("africa_quiz.html")
    
@app.route('/asia_quiz')
def asia():
    return render_template("asia_quiz.html")
    
@app.route('/australia_quiz')
def australia():
    return render_template("australia_quiz.html")
    
@app.route('/europe_quiz')
def europe():
    return render_template("europe_quiz.html")
    
@app.route('/n_america_quiz')
def n_america():
    return render_template("n_america_quiz.html")

@app.route('/s_america_quiz')
def s_america():
    return render_template("s_america_quiz.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
def quiz():
    print("where will this print to??")