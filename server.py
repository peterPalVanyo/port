from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<username>/<int:id>')
def hello_world(username, id=None):
    return render_template("index.html", username=username, id=id)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return "this is my blog!!!!!"