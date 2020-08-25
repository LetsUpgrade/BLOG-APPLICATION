from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/blog")
def blog():
    return render_template("inner_blog.html")

@app.route("/create")
def create():
    return render_template("create_blog.html")

@app.route("/setting")
def setting():
    return render_template("Setting.html")


app.run(debug=True)