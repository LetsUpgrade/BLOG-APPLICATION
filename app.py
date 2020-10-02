from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/blogapp"
db = SQLAlchemy(app)

class profile(db.Model):
    id = db.Column(db.String(25), primary_key=True)
    dp = db.Column(db.String(25), nullable=False)
    name = db.Column(db.String(35), nullable=False)
    bio = db.Column(db.String(100), nullable=False)
    followers = db.Column(db.Integer, nullable=False)
    following = db.Column(db.Integer, nullable=False)
    postno = db.Column(db.Integer, nullable=False)

class blogs(db.Model):
    id = db.Column(db.String(25), nullable= False)
    title = db.Column(db.String(25), nullable=False)
    content = db.Column(db.String(2500), nullable=False)
    image = db.Column(db.String(25), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    slug = db.Column(db.String(25), primary_key=True)



@app.route("/")
def home():
    return render_template("base.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup1.html")

@app.route("/create")
def create():
    return render_template("create_blog.html")

@app.route("/setting")
def setting():
    return render_template("Setting.html")

@app.route("/profile/<string:id>")
def profilefn(id):
    prof = profile.query.filter_by(id=id).first()
    blog = blogs.query.filter(blogs.slug.startswith(id)).all()
    return render_template("profile.html", prof=prof, blog=blog)

@app.route("/<string:slug>")
def post(slug):
    
    blog = blogs.query.filter_by(slug=slug).first()
    prof = profile.query.filter_by(id=blogs.id).first()
    date_posted = blog.date.strftime('%B %d, %Y')
    return render_template("inner_blog.html", blog=blog, prof=prof, date_posted=date_posted)


app.run(debug=True)