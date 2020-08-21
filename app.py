from flask import Flask, render_template, url_for

app = Flask(__name__)



@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/")
def create():
    return render_template("create_blog.html")

app.run(debug=True)