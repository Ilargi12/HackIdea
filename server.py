from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "<center> MAIN PAGE <h1> HELLO </h1> </center>"


@app.route("/<name>/")
def user(name):
    return f"<center> <h1> Hello {name}! </h1> </center>"


@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin"))


if __name__ == '__main__':
    app.run()