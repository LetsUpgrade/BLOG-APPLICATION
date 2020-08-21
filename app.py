from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/header")
def head():
    return render_template("header&footer.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/create")
def create():
    return render_template("create_blog.html")

app.run(debug=True)