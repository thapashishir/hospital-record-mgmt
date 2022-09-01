import flask

from web_app import app

@app.route("/")
def home():
    print("server fire")
    return flask.render_template("index.html")


@app.route("/appointments")
def add():
    return flask.render_template("appointments.html")
