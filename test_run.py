import os
import json
from flask import Flask, render_template, redirect, request

app = Flask(__name__)



""" Routing for Index.html """

""" need a different routing for each submit button on each modal ?? """

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
        score = 0
        user_answer = request.form["user_answer"]
        """attempting to set variable to the value of that from the json file """
        correct_answer = data['answer']
        
        
        """ below code will only write to file if correct answer is provided """
        
        if user_answer == correct_answer:
            with open("data/africa/africa_correct.json", "a") as answer:
                answer.write(request.form["user_answer"] + "\n")
                score +=1
            
        else:
            with open("data/africa/africa_incorrect.json", "a") as answer:
                answer.write(request.form["user_answer"] + "\n")
                
    
    
    """ following code found on stackoverflow """
    """ hoping to use it to sort the "scores" json data file - may not be what I'm looking for"""
                
    def extract_time(json):
        try:
        # Also convert to int since update_time will be string.  When comparing
        # strings, "10" is smaller than "2".
            return int(json['page']['update_time'])
        except KeyError:
            return 0

    # lines.sort() is more efficient than lines = lines.sorted()
    """ lines.sort(key=extract_time, reverse=True) """
        
    
    
    return render_template("africa_quiz.html", region="Africa", africa_data=data)


""" possibly no need for the following section as it is all covered above under the routing for "africa_username" """
    
@app.route('/africa_quiz')
def africa():
    data = []
    with open("data/africa/africa_quiz.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("africa_quiz.html", region="Africa", africa_data=data)











""" Routing for Asia Quiz Data """  
    
@app.route('/asia_get_user', methods=["GET", "POST"]    )
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