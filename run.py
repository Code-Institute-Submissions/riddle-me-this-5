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


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)