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


def get_africa_incorrect_list():
    list_incorrect = []
    with open("data/africa/africa_incorrect.txt", "r") as list_incorrect:
        list_incorrect = [row for row in list_incorrect]
        return list_incorrect[-10:]

"""
Get ALL correct answers
"""


def get_africa_correct_list():
    list_correct = []
    with open("data/africa/africa_correct.txt", "r") as list_correct:
        list_correct = [row for row in list_correct]
        return list_correct[-10:]

"""
Get final score
"""


def get_africa_score():
    final_score = []
    with open("data/africa/africa_final_score.txt", "r") as final_score:
        final_score = [row for row in final_score]
        return final_score

"""
Get Username for final score
"""


def get_africa_username():
    final_username = []
    with open("data/africa/africa_users.txt", "r") as final_username:
        final_username = [row for row in final_username]
        return final_username


""" Routing """


@app.route('/africa_get_user', methods=["GET", "POST"])
def africa_get_user():
    if request.method == "POST":
        os.remove("data/africa/africa_users.txt")  # removes file and previous data
        with open("data/africa/africa_users.txt", "a") as user_list:
            user_list.write(request.form["africa_username"] + "\n")
            os.remove("data/africa/africa_incorrect.txt")  # removes file and previous data
            os.remove("data/africa/africa_last_incorrect.txt")  # removes file and previous data
            os.remove("data/africa/africa_correct.txt")  # removes file and previous data
            os.remove("data/africa/africa_final_score.txt")  # removes file and previous data
        return redirect(request.form["africa_username"])
    return render_template("africa_get_user.html", region="Africa")


@app.route('/<africa_username>', methods=["GET", "POST"])
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
                    submit_score = {"Score": request.form["score"], "Username": africa_username}
                    json.dump(submit_score, open("data/africa/africa_scoreboard.json", "a"))
                    with open("data/africa/africa_final_score.txt", "a") as answer:
                            answer.write(request.form["score"] + "\n")
                            return redirect("africa_end")

    incorrect_answer = get_africa_incorrect_answer()

    return render_template("africa_quiz.html", region="Africa", africa_data=data, username=africa_username, score=score, index=index, incorrect_answer=incorrect_answer, message1="is incorrect! The correct answer was", message2="Try The Next Question!", correct_answer=data[index]['answer'], previous_answer=data[index-1]['answer'])


@app.route('/africa_end')
def africa_end():
    final_score = get_africa_score()
    incorrect_list = get_africa_incorrect_list()
    correct_list = get_africa_correct_list()
    username = get_africa_username()
    return render_template("africa_end.html", final_score=final_score, incorrect_list=incorrect_list, correct_list=correct_list, region="Africa", username=username)


"""
Asia Quiz Data
"""

"""
Get LAST incorrect answers
"""


def get_asia_incorrect_answer():  # work around for displaying Incorrect Message to User, notifying them of correct answer
    answers = []
    with open("data/asia/asia_last_incorrect.txt", "r") as incorrect_answer:
        answers = [row for row in incorrect_answer]
        return answers[-1:]

"""
Get ALL incorrect answers
"""


def get_asia_incorrect_list():
    list_incorrect = []
    with open("data/asia/asia_incorrect.txt", "r") as list_incorrect:
        list_incorrect = [row for row in list_incorrect]
        return list_incorrect[-10:]

"""
Get ALL correct answers
"""


def get_asia_correct_list():
    list_correct = []
    with open("data/asia/asia_correct.txt", "r") as list_correct:
        list_correct = [row for row in list_correct]
        return list_correct[-10:]

"""
Get final score
"""


def get_asia_score():
    final_score = []
    with open("data/asia/asia_final_score.txt", "r") as final_score:
        final_score = [row for row in final_score]
        return final_score

"""
Get Username for final score
"""


def get_asia_username():
    final_username = []
    with open("data/asia/asia_users.txt", "r") as final_username:
        final_username = [row for row in final_username]
        return final_username


""" Routing """


@app.route('/asia_get_user', methods=["GET", "POST"])
def asia_get_user():
    if request.method == "POST":
        os.remove("data/asia/asia_users.txt")  # removes file and previous data
        with open("data/asia/asia_users.txt", "a") as user_list:
            user_list.write(request.form["asia_username"] + "\n")
            os.remove("data/asia/asia_incorrect.txt")  # removes file and previous data
            os.remove("data/asia/asia_last_incorrect.txt")  # removes file and previous data
            os.remove("data/asia/asia_correct.txt")  # removes file and previous data
            os.remove("data/asia/asia_final_score.txt")  # removes file and previous data
        return redirect(request.form["asia_username"])
    return render_template("asia_get_user.html", region="Asia")


@app.route('/<asia_username>', methods=["GET", "POST"])
def asia_user(asia_username):
    data = []
    with open("data/asia/asia_quiz.json", "r") as json_data:
        data = json.load(json_data)
        index = 0  # set index to first question in json data file
        score = 0  # set score to 0
        correct_answer = data[index]['answer']  # sets variable to the value of 'answer' from the json file, for the specific index
        open("data/asia/asia_incorrect.txt", "a")  # creates blank data file to write incorret answers to
        open("data/asia/asia_last_incorrect.txt", "w")  # creates blank data file to write incorret answers to
        open("data/asia/asia_correct.txt", "a")  # creates blank data file to write incorret answers to
        open("data/asia/asia_final_score.txt", "a")  # creates blank data file to write incorret answers to

        if request.method == "POST":
            index = int(request.form["index"])
            score = int(request.form["score"])
            correct_answer = (request.form["correct_answer"])
            user_answer = request.form["user_answer"].title()

            if user_answer == correct_answer:
                index += 1  # incremements the index to the next question if the answer is correct
                with open("data/asia/asia_correct.txt", "a") as answer:
                    answer.write(request.form["user_answer"] + "\n")
                score += 1  # incremements the score x 1 if the answer is correct

            else:
                with open("data/asia/asia_last_incorrect.txt", "w") as answer:
                    answer.write(request.form["user_answer"].title() + "\n")  # work around for displaying Incorrect Message to User, notifying them of correct answer
                with open("data/asia/asia_incorrect.txt", "a") as answer:
                    answer.write(request.form["user_answer"].title() + "\n")
                index += 1
                score = score

            if request.method == "POST":  # code for finished quiz once all questions have been asked and enter final score in scoreboard
                if index >= 9:
                    submit_score = {"Score": request.form["score"], "Username": asia_username}
                    json.dump(submit_score, open("data/asia/asia_scoreboard.json", "a"))
                    with open("data/asia/asia_final_score.txt", "a") as answer:
                            answer.write(request.form["score"] + "\n")
                            return redirect("asia_end")

    incorrect_answer = get_asia_incorrect_answer()

    return render_template("asia_quiz.html", region="Asia", asia_data=data, username=asia_username, score=score, index=index, incorrect_answer=incorrect_answer, message1="is incorrect! The correct answer was", message2="Try The Next Question!", correct_answer=data[index]['answer'], previous_answer=data[index-1]['answer'])


@app.route('/asia_end')
def asia_end():
    final_score = get_asia_score()
    incorrect_list = get_asia_incorrect_list()
    correct_list = get_asia_correct_list()
    username = get_asia_username()
    return render_template("asia_end.html", final_score=final_score, incorrect_list=incorrect_list, correct_list=correct_list, region="Asia", username=username)


"""
Australia Quiz Data
"""

"""
Get LAST incorrect answers
"""


def get_australia_incorrect_answer():  # work around for displaying Incorrect Message to User, notifying them of correct answer
    answers = []
    with open("data/australia/australia_last_incorrect.txt", "r") as incorrect_answer:
        answers = [row for row in incorrect_answer]
        return answers[-1:]

"""
Get ALL incorrect answers
"""


def get_australia_incorrect_list():
    list_incorrect = []
    with open("data/australia/australia_incorrect.txt", "r") as list_incorrect:
        list_incorrect = [row for row in list_incorrect]
        return list_incorrect[-10:]

"""
Get ALL correct answers
"""


def get_australia_correct_list():
    list_correct = []
    with open("data/australia/australia_correct.txt", "r") as list_correct:
        list_correct = [row for row in list_correct]
        return list_correct[-10:]

"""
Get final score
"""


def get_australia_score():
    final_score = []
    with open("data/australia/australia_final_score.txt", "r") as final_score:
        final_score = [row for row in final_score]
        return final_score

"""
Get Username for final score
"""


def get_australia_username():
    final_username = []
    with open("data/australia/australia_users.txt", "r") as final_username:
        final_username = [row for row in final_username]
        return final_username


""" Routing """


@app.route('/australia_get_user', methods=["GET", "POST"])
def australia_get_user():
    if request.method == "POST":
        os.remove("data/australia/australia_users.txt")  # removes file and previous data
        with open("data/australia/australia_users.txt", "a") as user_list:
            user_list.write(request.form["australia_username"] + "\n")
            os.remove("data/australia/australia_incorrect.txt")  # removes file and previous data
            os.remove("data/australia/australia_last_incorrect.txt")  # removes file and previous data
            os.remove("data/australia/australia_correct.txt")  # removes file and previous data
            os.remove("data/australia/australia_final_score.txt")  # removes file and previous data
        return redirect(request.form["australia_username"])
    return render_template("australia_get_user.html", region="Australia")


@app.route('/<australia_username>', methods=["GET", "POST"])
def australia_user(australia_username):
    data = []
    with open("data/australia/australia_quiz.json", "r") as json_data:
        data = json.load(json_data)
        index = 0  # set index to first question in json data file
        score = 0  # set score to 0
        correct_answer = data[index]['answer']  # sets variable to the value of 'answer' from the json file, for the specific index
        open("data/australia/australia_incorrect.txt", "a")  # creates blank data file to write incorret answers to
        open("data/australia/australia_last_incorrect.txt", "w")  # creates blank data file to write incorret answers to
        open("data/australia/australia_correct.txt", "a")  # creates blank data file to write incorret answers to
        open("data/australia/australia_final_score.txt", "a")  # creates blank data file to write incorret answers to

        if request.method == "POST":
            index = int(request.form["index"])
            score = int(request.form["score"])
            correct_answer = (request.form["correct_answer"])
            user_answer = request.form["user_answer"].title()

            if user_answer == correct_answer:
                index += 1  # incremements the index to the next question if the answer is correct
                with open("data/australia/australia_correct.txt", "a") as answer:
                    answer.write(request.form["user_answer"] + "\n")
                score += 1  # incremements the score x 1 if the answer is correct

            else:
                with open("data/australia/australia_last_incorrect.txt", "w") as answer:
                    answer.write(request.form["user_answer"].title() + "\n")  # work around for displaying Incorrect Message to User, notifying them of correct answer
                with open("data/australia/australia_incorrect.txt", "a") as answer:
                    answer.write(request.form["user_answer"].title() + "\n")
                index += 1
                score = score

            if request.method == "POST":  # code for finished quiz once all questions have been asked and enter final score in scoreboard
                if index >= 10:
                    submit_score = {"Score": request.form["score"], "Username": australia_username}
                    json.dump(submit_score, open("data/australia/australia_scoreboard.json", "a"))
                    with open("data/australia/australia_final_score.txt", "a") as answer:
                            answer.write(request.form["score"] + "\n")
                            return redirect("australia_end")

    incorrect_answer = get_australia_incorrect_answer()

    return render_template("australia_quiz.html", region="Australia", australia_data=data, username=australia_username, score=score, index=index, incorrect_answer=incorrect_answer, message1="is incorrect! The correct answer was", message2="Try The Next Question!", correct_answer=data[index]['answer'], previous_answer=data[index-1]['answer'])


@app.route('/australia_end')
def australia_end():
    final_score = get_australia_score()
    incorrect_list = get_australia_incorrect_list()
    correct_list = get_australia_correct_list()
    username = get_australia_username()
    return render_template("australia_end.html", final_score=final_score, incorrect_list=incorrect_list, correct_list=correct_list, region="Australia", username=username)


"""
Europe Quiz Data
"""

"""
Get LAST incorrect answers
"""


def get_europe_incorrect_answer():  # work around for displaying Incorrect Message to User, notifying them of correct answer
    answers = []
    with open("data/europe/europe_last_incorrect.txt", "r") as incorrect_answer:
        answers = [row for row in incorrect_answer]
        return answers[-1:]

"""
Get ALL incorrect answers
"""


def get_europe_incorrect_list():
    list_incorrect = []
    with open("data/europe/europe_incorrect.txt", "r") as list_incorrect:
        list_incorrect = [row for row in list_incorrect]
        return list_incorrect[-10:]

"""
Get ALL correct answers
"""


def get_europe_correct_list():
    list_correct = []
    with open("data/europe/europe_correct.txt", "r") as list_correct:
        list_correct = [row for row in list_correct]
        return list_correct[-10:]

"""
Get final score
"""


def get_europe_score():
    final_score = []
    with open("data/europe/europe_final_score.txt", "r") as final_score:
        final_score = [row for row in final_score]
        return final_score

"""
Get Username for final score
"""


def get_europe_username():
    final_username = []
    with open("data/europe/europe_users.txt", "r") as final_username:
        final_username = [row for row in final_username]
        return final_username


""" Routing """


@app.route('/europe_get_user', methods=["GET", "POST"])
def europe_get_user():
    if request.method == "POST":
        os.remove("data/europe/europe_users.txt")  # removes file and previous data
        with open("data/europe/europe_users.txt", "a") as user_list:
            user_list.write(request.form["europe_username"] + "\n")
            os.remove("data/europe/europe_incorrect.txt")  # removes file and previous data
            os.remove("data/europe/europe_last_incorrect.txt")  # removes file and previous data
            os.remove("data/europe/europe_correct.txt")  # removes file and previous data
            os.remove("data/europe/europe_final_score.txt")  # removes file and previous data
        return redirect(request.form["europe_username"])
    return render_template("europe_get_user.html", region="Europe")


@app.route('/<europe_username>', methods=["GET", "POST"])
def europe_user(europe_username):
    data = []
    with open("data/europe/europe_quiz.json", "r") as json_data:
        data = json.load(json_data)
        index = 0  # set index to first question in json data file
        score = 0  # set score to 0
        correct_answer = data[index]['answer']  # sets variable to the value of 'answer' from the json file, for the specific index
        open("data/europe/europe_incorrect.txt", "a")  # creates blank data file to write incorret answers to
        open("data/europe/europe_last_incorrect.txt", "w")  # creates blank data file to write incorret answers to
        open("data/europe/europe_correct.txt", "a")  # creates blank data file to write incorret answers to
        open("data/europe/europe_final_score.txt", "a")  # creates blank data file to write incorret answers to

        if request.method == "POST":
            index = int(request.form["index"])
            score = int(request.form["score"])
            correct_answer = (request.form["correct_answer"])
            user_answer = request.form["user_answer"].title()

            if user_answer == correct_answer:
                index += 1  # incremements the index to the next question if the answer is correct
                with open("data/europe/europe_correct.txt", "a") as answer:
                    answer.write(request.form["user_answer"] + "\n")
                score += 1  # incremements the score x 1 if the answer is correct

            else:
                with open("data/europe/europe_last_incorrect.txt", "w") as answer:
                    answer.write(request.form["user_answer"].title() + "\n")  # work around for displaying Incorrect Message to User, notifying them of correct answer
                with open("data/europe/europe_incorrect.txt", "a") as answer:
                    answer.write(request.form["user_answer"].title() + "\n")
                index += 1
                score = score

            if request.method == "POST":  # code for finished quiz once all questions have been asked and enter final score in scoreboard
                if index >= 10:
                    submit_score = {"Score": request.form["score"], "Username": europe_username}
                    json.dump(submit_score, open("data/europe/europe_scoreboard.json", "a"))
                    with open("data/europe/europe_final_score.txt", "a") as answer:
                            answer.write(request.form["score"] + "\n")
                            return redirect("europe_end")

    incorrect_answer = get_europe_incorrect_answer()

    return render_template("europe_quiz.html", region="Europe", europe_data=data, username=europe_username, score=score, index=index, incorrect_answer=incorrect_answer, message1="is incorrect! The correct answer was", message2="Try The Next Question!", correct_answer=data[index]['answer'], previous_answer=data[index-1]['answer'])


@app.route('/europe_end')
def europe_end():
    final_score = get_europe_score()
    incorrect_list = get_europe_incorrect_list()
    correct_list = get_europe_correct_list()
    username = get_europe_username()
    return render_template("europe_end.html", final_score=final_score, incorrect_list=incorrect_list, correct_list=correct_list, region="Europe", username=username)


"""
North America Quiz Data
"""

"""
Get LAST incorrect answers
"""


def get_n_america_incorrect_answer():  # work around for displaying Incorrect Message to User, notifying them of correct answer
    answers = []
    with open("data/n_america/n_america_last_incorrect.txt", "r") as incorrect_answer:
        answers = [row for row in incorrect_answer]
        return answers[-1:]

"""
Get ALL incorrect answers
"""


def get_n_america_incorrect_list():
    list_incorrect = []
    with open("data/n_america/n_america_incorrect.txt", "r") as list_incorrect:
        list_incorrect = [row for row in list_incorrect]
        return list_incorrect[-10:]

"""
Get ALL correct answers
"""


def get_n_america_correct_list():
    list_correct = []
    with open("data/n_america/n_america_correct.txt", "r") as list_correct:
        list_correct = [row for row in list_correct]
        return list_correct[-10:]

"""
Get final score
"""


def get_n_america_score():
    final_score = []
    with open("data/n_america/n_america_final_score.txt", "r") as final_score:
        final_score = [row for row in final_score]
        return final_score

"""
Get Username for final score
"""


def get_n_america_username():
    final_username = []
    with open("data/n_america/n_america_users.txt", "r") as final_username:
        final_username = [row for row in final_username]
        return final_username


""" Routing """


@app.route('/n_america_get_user', methods=["GET", "POST"])
def n_america_get_user():
    if request.method == "POST":
        os.remove("data/n_america/n_america_users.txt")  # removes file and previous data
        with open("data/n_america/n_america_users.txt", "a") as user_list:
            user_list.write(request.form["n_america_username"] + "\n")
            os.remove("data/n_america/n_america_incorrect.txt")  # removes file and previous data
            os.remove("data/n_america/n_america_last_incorrect.txt")  # removes file and previous data
            os.remove("data/n_america/n_america_correct.txt")  # removes file and previous data
            os.remove("data/n_america/n_america_final_score.txt")  # removes file and previous data
        return redirect(request.form["n_america_username"])
    return render_template("n_america_get_user.html", region="N_america")


@app.route('/<n_america_username>', methods=["GET", "POST"])
def n_america_user(n_america_username):
    data = []
    with open("data/n_america/n_america_quiz.json", "r") as json_data:
        data = json.load(json_data)
        index = 0  # set index to first question in json data file
        score = 0  # set score to 0
        correct_answer = data[index]['answer']  # sets variable to the value of 'answer' from the json file, for the specific index
        open("data/n_america/n_america_incorrect.txt", "a")  # creates blank data file to write incorret answers to
        open("data/n_america/n_america_last_incorrect.txt", "w")  # creates blank data file to write incorret answers to
        open("data/n_america/n_america_correct.txt", "a")  # creates blank data file to write incorret answers to
        open("data/n_america/n_america_final_score.txt", "a")  # creates blank data file to write incorret answers to

        if request.method == "POST":
            index = int(request.form["index"])
            score = int(request.form["score"])
            correct_answer = (request.form["correct_answer"])
            user_answer = request.form["user_answer"].title()

            if user_answer == correct_answer:
                index += 1  # incremements the index to the next question if the answer is correct
                with open("data/n_america/n_america_correct.txt", "a") as answer:
                    answer.write(request.form["user_answer"] + "\n")
                score += 1  # incremements the score x 1 if the answer is correct

            else:
                with open("data/n_america/n_america_last_incorrect.txt", "w") as answer:
                    answer.write(request.form["user_answer"].title() + "\n")  # work around for displaying Incorrect Message to User, notifying them of correct answer
                with open("data/n_america/n_america_incorrect.txt", "a") as answer:
                    answer.write(request.form["user_answer"].title() + "\n")
                index += 1
                score = score

            if request.method == "POST":  # code for finished quiz once all questions have been asked and enter final score in scoreboard
                if index >= 10:
                    submit_score = {"Score": request.form["score"], "Username": n_america_username}
                    json.dump(submit_score, open("data/n_america/n_america_scoreboard.json", "a"))
                    with open("data/n_america/n_america_final_score.txt", "a") as answer:
                            answer.write(request.form["score"] + "\n")
                            return redirect("n_america_end")

    incorrect_answer = get_n_america_incorrect_answer()

    return render_template("n_america_quiz.html", region="N_america", n_america_data=data, username=n_america_username, score=score, index=index, incorrect_answer=incorrect_answer, message1="is incorrect! The correct answer was", message2="Try The Next Question!", correct_answer=data[index]['answer'], previous_answer=data[index-1]['answer'])


@app.route('/n_america_end')
def n_america_end():
    final_score = get_n_america_score()
    incorrect_list = get_n_america_incorrect_list()
    correct_list = get_n_america_correct_list()
    username = get_n_america_username()
    return render_template("n_america_end.html", final_score=final_score, incorrect_list=incorrect_list, correct_list=correct_list, region="N_america", username=username)


"""
South America Quiz Data
"""

"""
Get LAST incorrect answers
"""


def get_s_america_incorrect_answer():  # work around for displaying Incorrect Message to User, notifying them of correct answer
    answers = []
    with open("data/s_america/s_america_last_incorrect.txt", "r") as incorrect_answer:
        answers = [row for row in incorrect_answer]
        return answers[-1:]

"""
Get ALL incorrect answers
"""


def get_s_america_incorrect_list():
    list_incorrect = []
    with open("data/s_america/s_america_incorrect.txt", "r") as list_incorrect:
        list_incorrect = [row for row in list_incorrect]
        return list_incorrect[-10:]

"""
Get ALL correct answers
"""


def get_s_america_correct_list():
    list_correct = []
    with open("data/s_america/s_america_correct.txt", "r") as list_correct:
        list_correct = [row for row in list_correct]
        return list_correct[-10:]

"""
Get final score
"""


def get_s_america_score():
    final_score = []
    with open("data/s_america/s_america_final_score.txt", "r") as final_score:
        final_score = [row for row in final_score]
        return final_score

"""
Get Username for final score
"""


def get_s_america_username():
    final_username = []
    with open("data/s_america/s_america_users.txt", "r") as final_username:
        final_username = [row for row in final_username]
        return final_username


""" Routing """


@app.route('/s_america_get_user', methods=["GET", "POST"])
def s_america_get_user():
    if request.method == "POST":
        os.remove("data/s_america/s_america_users.txt")  # removes file and previous data
        with open("data/s_america/s_america_users.txt", "a") as user_list:
            user_list.write(request.form["s_america_username"] + "\n")
            os.remove("data/s_america/s_america_incorrect.txt")  # removes file and previous data
            os.remove("data/s_america/s_america_last_incorrect.txt")  # removes file and previous data
            os.remove("data/s_america/s_america_correct.txt")  # removes file and previous data
            os.remove("data/s_america/s_america_final_score.txt")  # removes file and previous data
        return redirect(request.form["s_america_username"])
    return render_template("s_america_get_user.html", region="S_america")


@app.route('/<s_america_username>', methods=["GET", "POST"])
def s_america_user(s_america_username):
    data = []
    with open("data/s_america/s_america_quiz.json", "r") as json_data:
        data = json.load(json_data)
        index = 0  # set index to first question in json data file
        score = 0  # set score to 0
        correct_answer = data[index]['answer']  # sets variable to the value of 'answer' from the json file, for the specific index
        open("data/s_america/s_america_incorrect.txt", "a")  # creates blank data file to write incorret answers to
        open("data/s_america/s_america_last_incorrect.txt", "w")  # creates blank data file to write incorret answers to
        open("data/s_america/s_america_correct.txt", "a")  # creates blank data file to write incorret answers to
        open("data/s_america/s_america_final_score.txt", "a")  # creates blank data file to write incorret answers to

        if request.method == "POST":
            index = int(request.form["index"])
            score = int(request.form["score"])
            correct_answer = (request.form["correct_answer"])
            user_answer = request.form["user_answer"].title()

            if user_answer == correct_answer:
                index += 1  # incremements the index to the next question if the answer is correct
                with open("data/s_america/s_america_correct.txt", "a") as answer:
                    answer.write(request.form["user_answer"] + "\n")
                score += 1  # incremements the score x 1 if the answer is correct

            else:
                with open("data/s_america/s_america_last_incorrect.txt", "w") as answer:
                    answer.write(request.form["user_answer"].title() + "\n")  # work around for displaying Incorrect Message to User, notifying them of correct answer
                with open("data/s_america/s_america_incorrect.txt", "a") as answer:
                    answer.write(request.form["user_answer"].title() + "\n")
                index += 1
                score = score

            if request.method == "POST":  # code for finished quiz once all questions have been asked and enter final score in scoreboard
                if index >= 10:
                    submit_score = {"Score": request.form["score"], "Username": s_america_username}
                    json.dump(submit_score, open("data/s_america/s_america_scoreboard.json", "a"))
                    with open("data/s_america/s_america_final_score.txt", "a") as answer:
                            answer.write(request.form["score"] + "\n")
                            return redirect("s_america_end")

    incorrect_answer = get_s_america_incorrect_answer()

    return render_template("s_america_quiz.html", region="S_america", s_america_data=data, username=s_america_username, score=score, index=index, incorrect_answer=incorrect_answer, message1="is incorrect! The correct answer was", message2="Try The Next Question!", correct_answer=data[index]['answer'], previous_answer=data[index-1]['answer'])


@app.route('/s_america_end')
def s_america_end():
    final_score = get_s_america_score()
    incorrect_list = get_s_america_incorrect_list()
    correct_list = get_s_america_correct_list()
    username = get_s_america_username()
    return render_template("s_america_end.html", final_score=final_score, incorrect_list=incorrect_list, correct_list=correct_list, region="S_america", username=username)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
