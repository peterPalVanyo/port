from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template("index.html")


@app.route("/<string:page>")
def page(page):
    return render_template(page)


# @app.route('/components.html')
# def components():
#     return render_template("components.html")

