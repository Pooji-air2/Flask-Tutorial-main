from flask import Flask, render_template, request

app = Flask(__name__)

icecreams = ['Chcolate',
             'Blueberry',
             'Belgium Chcolate',
             'Triple Chcolate',
             'Caramel Salt',
             'Blackberry',
             'Strawberry',
            'Vanilla']

@app.route("/")
def index():
   return render_template("index.html", icecreams=icecreams)
