import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    today = datetime.datetime.today().weekday()
    answer = "NO"
    if today == 5:
        answer = "Yes"
    return render_template("index.html", answer=answer)
