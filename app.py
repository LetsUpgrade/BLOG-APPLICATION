from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/blogapp"
db = SQLAlchemy(app)

class profile(db.Model):
    id = db.Column(db.String(25), primary_key=True)
    name = db.Column(db.String(35), nullable=False)
    bio = db.Column(db.String(100), nullable=False)
    followers = db.Column(db.Integer, nullable=False)
    following = db.Column(db.Integer, nullable=False)
    postno = db.Column(db.Integer, nullable=False)


@app.route("/")
def home():
    return render_template("base.html")


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

@app.route("/profile/<string:id>")
def profilefn(id):
    prof = profile.query.filter_by(id=id).first()
    return render_template("profile.html", prof=prof)


app.run(debug=True)