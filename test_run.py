import os
import json
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


""" 
Routing for Index.html 
"""

@app.route('/')
def index():
        return render_template("index.html")

index = 0
score = 0

""" 
Africa Quiz Data 
"""

""" 
Get all incorrect answers
"""
def get_africa_incorrect_answers():
	answers = []
	with open("data/africa/africa_incorrect.json", "r") as incorrect_answers:
			answers = [row for row in incorrect_answers]
			return answers[-1:]
			

""" Routing """

@app.route('/africa_get_user', methods=["GET", "POST"])
def africa_get_user():
    if request.method == "POST":
        with open("data/africa/africa_users.json", "a") as user_list:
            user_list.write(request.form["africa_username"] + "\n")
            os.remove("data/africa/africa_incorrect.json") # removes file and previous data
        return redirect(request.form["africa_username"])
    return render_template("africa_get_user.html", region="Africa")
    

@app.route('/<africa_username>', methods=["GET", "POST"])
def africa_user(africa_username):
    data = []
    with open("data/africa/africa_quiz.json", "r") as json_data:
        data = json.load(json_data)
        index = 0 # set index to first question in json data file
        score = 0 # set score to 0
        open("data/africa/africa_incorrect.json", "w") # creates blank data file to write incorret answers to
        
    
        if request.method == "POST":
            user_answer = request.form["user_answer"]
            correct_answer = data[index]['answer'] # sets variable to the value of 'answer' from the json file, for the specific index
            
            if user_answer == correct_answer:
                index +=1 # incremements the index to the next question if the answer is correct
                submit_correct = {"Answer": request.form["user_answer"], "Username": africa_username}
                json.dump(submit_correct, open("data/africa/africa_correct.json","a"))
                #with open("data/africa/africa_correct.json", "a") as answer:
                #answer.write(request.form["user_answer"] + "\n")
                score +=1 # incremements the score x 1 if the answer is correct
            
            else:
                with open("data/africa/africa_incorrect.json", "a") as answer:
                    answer.write(request.form["user_answer"] + "\n")
                correct_answer = data[index]['answer']
                index+=1
    
    incorrect_answers = get_africa_incorrect_answers()
    
    return render_template("africa_quiz.html", region = "Africa", africa_data = data, username = africa_username, score = score, index = index, incorrect_answers = incorrect_answers, message1 = "is incorrect! The correct answer was", message2 = "Try The Next Question!", correct_answer = data[index]['answer'], previous_answer = data[index-1]['answer'])


""" 
Routing for Asia Quiz Data
"""

@app.route('/asia_get_user', methods=["GET", "POST"])
def asia_get_user():
    if request.method == "POST":
        with open("data/asia/asia_users.json", "a") as user_list:
            user_list.write(request.form["asia_username"] + "\n")
        return redirect(request.form["asia_username"])
    return render_template("asia_get_user.html", region="Asia")
    
@app.route('/<asia_username>', methods=["GET", "POST"])
def asia_user(asia_username):
    data = []
    with open("data/asia/asia_quiz.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("asia_quiz.html", region="Asia", asia_data=data)
    
    
    
    
    
    
""" 
Routing for Australia Quiz Data
"""  

@app.route('/australia_get_user', methods=["GET", "POST"])
def australia_get_user():
    if request.method == "POST":
        with open("data/australia/australia_users.json", "a") as user_list:
            user_list.write(request.form["australia_username"] + "\n")
        return redirect(request.form["australia_username"])
    return render_template("australia_get_user.html", region="Australia")
    
@app.route('/<australia_username>', methods=["GET", "POST"])
def australia_user(australia_username):
    data = []
    with open("data/austarlia/australia_quiz.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("australia_quiz.html", region="Australia", australia_data=data)
    

    

""" 
Routing for Europe Quiz Data
"""

@app.route('/europe_get_user', methods=["GET", "POST"])
def europe_get_user():
    if request.method == "POST":
        with open("data/europe/europe_users.json", "a") as user_list:
            user_list.write(request.form["europe_username"] + "\n")
        return redirect(request.form["europe_username"])
    return render_template("europe_get_user.html", region="Europe")

@app.route('/<europe_username>', methods=["GET", "POST"])
def europe_user(europe_username):
    data = []
    with open("data/europe/europe_quiz.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("europe_quiz.html", region="Europe", europe_data=data)
    
    
    
    


""" 
Routing for N America Quiz Data
"""

@app.route('/n_america_get_user', methods=["GET", "POST"])
def n_america_get_user():
    if request.method == "POST":
        with open("data/n_america/n_america_users.json", "a") as user_list:
            user_list.write(request.form["n_america_username"] + "\n")
        return redirect(request.form["n_america_username"])
    return render_template("n_america_get_user.html", region="North America")
    

@app.route('/<n_america_username>', methods=["GET", "POST"])
def n_america_user(n_america_username):
    data = []
    with open("data/n_america/n_america_quiz.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("n_america_quiz.html", region="North America", n_america_data=data)
    
    
    
    


""" 
Routing for S America Quiz Data
""" 

@app.route('/s_america_get_user', methods=["GET", "POST"])
def s_america_get_user():
    if request.method == "POST":
        with open("data/s_america/s_america_users.json", "a") as user_list:
            user_list.write(request.form["s_america_username"] + "\n")
        return redirect(request.form["s_america_username"])
    return render_template("s_america_get_user.html", region="South America")
    

@app.route('/<s_america_username>', methods=["GET", "POST"])
def s_america_user(s_america_username):
    data = []
    with open("data/s_america/s_america_quiz.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("s_america_quiz.html", region="South America", s_america_data=data)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)