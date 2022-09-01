import email
import flask

from web_app import app

@app.route("/")
def home():
    print("server fire")
    return flask.render_template("index.html")


@app.route("/appointments")
def search():
    return flask.render_template("appointments.html")

@app.route("/appointment/add")
def add_get():
    return flask.render_template("add.html", email = None, password = None)

@app.route("/appointment/add", methods=["POST"])
def add_post():
    email = flask.request.form["email"]
    password = flask.request.form["password"]
    return flask.render_template("add.html", email = email, password = password )

