import os
import json
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


"""
Routing for Index.html
"""


@app.route('/')
def index():
    leader_africa = get_africa_leader()
    return render_template("index.html", leader_africa=leader_africa)


"""
Africa Quiz Data
"""

"""
Get LAST incorrect answers
"""


def get_africa_incorrect_answer():  # work around for displaying Incorrect Message to User, notifying them of correct answer
    answers = []
    with open("data/africa/africa_last_incorrect.txt", "r") as incorrect_answer:
        answers = [row for row in incorrect_answer]
        return answers[-1:]

"""
Get ALL incorrect answers
"""


def get_africa_incorrect_list():  # used to record a list of all incorrect answers
    list_incorrect = []
    with open("data/africa/africa_incorrect.txt", "r") as list_incorrect:
        list_incorrect = [row for row in list_incorrect]
        return list_incorrect[-10:]

"""
Get ALL correct answers
"""


def get_africa_correct_list():  # used to record a list of all correct answers
    list_correct = []
    with open("data/africa/africa_correct.txt", "r") as list_correct:
        list_correct = [row for row in list_correct]
        return list_correct[-10:]

"""
Get final score
"""


def get_africa_score():  # used to record the final score after the final question
    final_score = []
    with open("data/africa/africa_final_score.txt", "r") as final_score:
        final_score = [row for row in final_score]
        return final_score[-1:]

"""
Get Username for final score
"""


def get_africa_username():  # used to record the current username for display on 'Final Score' page
    final_username = []
    with open("data/africa/africa_users.txt", "r") as final_username:
        final_username = [row for row in final_username]
        return final_username[-1:]


"""
Get Leaderboard Data
"""


def get_africa_leaderboard():  # used to get the Leaderboard data from 'africa_leaderboard.json'
    africa_leaderboard = []
    with open("data/africa/africa_scoreboard.json", "r") as africa_leaderboard:
        africa_leaderboard = json.load(africa_leaderboard)
        #africa_leaderboard = [row for row in africa_leaderboard]
        return africa_leaderboard[-10:]


"""
Get Leader
"""

def get_africa_leader():  # used to get the Leaderboard data from 'africa_leaderboard.json'
    africa_leader = []
    with open("data/africa/africa_scoreboard.json", "r") as africa_leader:
        africa_leader = [row for row in africa_leader]
        return africa_leader[-1:]


""" Routing """


@app.route('/africa_get_user', methods=["GET", "POST"])
def africa_get_user():
    if request.method == "POST":
        os.remove("data/africa/africa_users.txt")  # removes file and previous data
        with open("data/africa/africa_users.txt", "a") as user_list:
            user_list.write(request.form["africa_username"])
            os.remove("data/africa/africa_incorrect.txt")  # removes file and previous data
            os.remove("data/africa/africa_last_incorrect.txt")  # removes file and previous data
            os.remove("data/africa/africa_correct.txt")  # removes file and previous data
            os.remove("data/africa/africa_final_score.txt")  # removes file and previous data
        return redirect(url_for('africa_user', africa_username = request.form["africa_username"]))
    return render_template("africa_get_user.html", region="Africa")


@app.route('/africa_username<africa_username>', methods=["GET", "POST"])
def africa_user(africa_username):
    data = []
    with open("data/africa/africa_quiz.json", "r") as json_data:
        data = json.load(json_data)
        index = 0  # set index to first question in json data file
        score = 0  # set score to 0
        correct_answer = data[index]['answer']  # sets variable to the value of 'answer' from the json file, for the specific index
        open("data/africa/africa_incorrect.txt", "a")  # creates blank data file to write incorret answers to
        open("data/africa/africa_last_incorrect.txt", "w")  # creates blank data file to write incorret answers to
        open("data/africa/africa_correct.txt", "a")  # creates blank data file to write incorret answers to
        open("data/africa/africa_final_score.txt", "a")  # creates blank data file to write incorret answers to

        if request.method == "POST":
            index = int(request.form["index"])
            score = int(request.form["score"])
            correct_answer = (request.form["correct_answer"])
            user_answer = request.form["user_answer"].title()

            if user_answer == correct_answer:
                index += 1  # incremements the index to the next question if the answer is correct
                with open("data/africa/africa_correct.txt", "a") as answer:
                    answer.write(request.form["user_answer"] + "\n")
                score += 1  # incremements the score x 1 if the answer is correct

            else:
                with open("data/africa/africa_last_incorrect.txt", "w") as answer:
                    answer.write(request.form["user_answer"].title() + "\n")  # work around for displaying Incorrect Message to User, notifying them of correct answer
                with open("data/africa/africa_incorrect.txt", "a") as answer:
                    answer.write(request.form["user_answer"].title() + "\n")
                index += 1
                score = score

            if request.method == "POST":  # code for finished quiz once all questions have been asked and enter final score in scoreboard
                if index >= 10:
                    score = int(request.form["score"])
                    correct_answer = (request.form["correct_answer"])
                    user_answer = request.form["user_answer"].title()
                    
                    if user_answer == correct_answer: # if answer is correct, update score and submit final score and username
                        score = int(request.form["score"])
                        score += 1
                        #submit_score = ({"Score": score, "Username": africa_username})
                        with open("data/africa/africa_scoreboard.json", "a") as json_file:
                            json.dump({"Score": score, "Username": africa_username}, json_file, indent=4)
                            json_file.write("\n")
                        with open("data/africa/africa_final_score.txt", "a") as answer:
                            answer.write(str(score))
                            
                    elif user_answer != correct_answer: # if answer is not correct, submit final score and username
                        #submit_score = ({"Score": request.form["score"], "Username": africa_username})
                        with open("data/africa/africa_scoreboard.json", "a") as json_file:
                            json.dump({"Score": score, "Username": africa_username}, json_file, indent=4)
                            json_file.write("\n")
                        with open("data/africa/africa_final_score.txt", "a") as answer:
                            answer.write(request.form["score"])
                            
                    return redirect("africa_end")

    incorrect_answer = get_africa_incorrect_answer()

    return render_template("africa_quiz.html", region="Africa", africa_data=data, username=africa_username, score=score, index=index, incorrect_answer=incorrect_answer, message1="is incorrect! The correct answer was", message2="Try The Next Question!", correct_answer=data[index]['answer'], previous_answer=data[index-1]['answer'])


@app.route('/africa_end')
def africa_end():
    final_score = get_africa_score()
    incorrect_list = get_africa_incorrect_list()
    correct_list = get_africa_correct_list()
    username = get_africa_username()
    leaderboard = sorted(get_africa_leaderboard(),reverse=True)
    return render_template("africa_end.html", final_score=final_score, incorrect_list=incorrect_list, correct_list=correct_list, region="Africa", username=username, leaderboard = leaderboard)


""" Other sections will be reinserted here once testing is complete - remember to fix the issue on routing
    see comments for commit 3340b77 - dated 11th Dec 2018
"""


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
