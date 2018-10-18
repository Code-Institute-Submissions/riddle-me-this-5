import os
import json
from flask import Flask, render_template, redirect, request

app = Flask(__name__)


"""
Reusable function for opening a file and writing to it
"""
def write_file(filename, message):
	with open (filename, 'a') as file:
		file.writelines(message + "\n")

""" Routing for Index.html """

@app.route('/', methods=["GET", "POST"])
def index():
    """Used to capture Username when START QUIZ button is selected"""
    if request.method == "POST":
        with open("data/africa/africa_users.json", "a") as user_list:
            user_list.write(request.form["africa_username"] + "\n")
        return redirect(request.form["africa_username"])
    else:
        return render_template("index.html")


""" Routing for Africa Quiz Data """    

@app.route('/<africa_username>', methods=["GET", "POST"])
def africa_user(africa_username):
    data = []
    with open("data/africa/africa_quiz.json", "r") as json_data:
        data = json.load(json_data)
        index = 0
     
        if request.method == "POST":
            with open("data/africa/africa_correct.json", "a") as answer:
                answer.write(request.form["user_answer"] + "\n")
            return redirect(request.form["user_answer"])
        
    return render_template("africa_quiz.html", region="Africa", africa_data=data)
        
    
@app.route('/africa_quiz')
def africa():
    data = []
    with open("data/africa/africa_quiz.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("africa_quiz.html", region="Africa", africa_data=data)










""" Routing for Asia Quiz Data """  

@app.route('/<asia_username>')
def asia_user(asia_username):
    data = []
    with open("data/asai/asia_quiz.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("asia_quiz.html", region="Asia", asia_data=data)
    
    
@app.route('/asia_quiz')
def asia():
    data=[]
    with open("data/asia/asia_quiz.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("asia_quiz.html", region="Asia", asia_data=data)


""" Routing for Australia Quiz Data """  
    
@app.route('/australia_quiz')
def australia():
    return render_template("australia_quiz.html", region="Australia")


""" Routing for Europe Quiz Data """  

@app.route('/europe_quiz')
def europe():
    return render_template("europe_quiz.html", region="Europe")


""" Routing for N America Quiz Data """  

@app.route('/n_america_quiz')
def n_america():
    return render_template("n_america_quiz.html", region="North America")


""" Routing for S America Quiz Data """  

@app.route('/s_america_quiz')
def s_america():
    return render_template("s_america_quiz.html", region="South America")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)