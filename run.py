import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/africa_quiz')
def africa():
    data = []
    with open("data/africa/africa_quiz.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("africa_quiz.html", region="Africa")
    
@app.route('/asia_quiz')
def asia():
    return render_template("asia_quiz.html", region="Asia")
    
@app.route('/australia_quiz')
def australia():
    return render_template("australia_quiz.html", region="Australia")
    
@app.route('/europe_quiz')
def europe():
    return render_template("europe_quiz.html", region="Europe")
    
@app.route('/n_america_quiz')
def n_america():
    return render_template("n_america_quiz.html", region="North America")

@app.route('/s_america_quiz')
def s_america():
    return render_template("s_america_quiz.html", region="South America")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
def quiz():
    print("where will this print to??")