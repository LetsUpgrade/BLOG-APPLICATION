from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/createblog'
db = SQLAlchemy(app)

class Blog_creation(db.Model):
    '''
    SNo,title, content
    '''
    SNo = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.String(500), unique=True, nullable=False)
    img_file = db.Column(db.String(500), unique=False, nullable=False)




@app.route("/", methods = ['GET','POST'])
def createblog():
    if(request.method=='POST'):
        title = request.form.get('title')
        content = request.form.get('content')
        img_file = request.form.get('img_file')
        entry = Blog_creation(title=title, content=content, img_file=img_file )


        db.session.add(entry)
        db.session.commit()




    return render_template('createblog.html')












app.run(debug=True)




