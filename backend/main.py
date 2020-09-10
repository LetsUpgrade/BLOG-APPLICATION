import pyrebase	
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
	

app = Flask(__name__)       

config = {
	  "apiKey": "",
	  "authDomain": "",
	  "databaseURL": "",
	  "storageBucket": "",
  	  "projectId": "",
  	  "messagingSenderId": "",
  	  "appId": "",
   	  "measurementId": ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
	

person = {"is_logged_in": False, "name": "", "email": "", "uid": ""}
	

#----------Home page
@app.route("/")
@app.route("/home")
def home():
	    return render_template("home.html")
	

#----------Login
@app.route("/login", methods = ["POST", "GET"])
def login():
	    if request.method == "POST":        
	        result = request.form           
	        email = result["email"]
	        password = result["pass"]
	        try:
	            user = auth.sign_in_with_email_and_password(email, password)
	            global person
	            person["is_logged_in"] = True
	            person["email"] = user["email"]
	            person["uid"] = user["localId"]

	            data = db.child("users").get()
	            person["name"] = data.val()[person["uid"]]["name"]

	            flash(f'You have been logged in.', 'success')
	            return redirect(url_for('home'))
	        except:
	            flash(f'Login unsuccessful.', 'danger')
	            return redirect(url_for('login'))
	    else:
	        if person["is_logged_in"] == True:
	        	flash(f'You have been logged in.', 'success')
	            return redirect(url_for('home'))
	        else:
	        	flash(f'Login unsuccessful.', 'danger')
	            return redirect(url_for('login'))

	return render_template("login.html")
	
#Sign up/ Register
@app.route("/signup", methods = ["POST", "GET"])
def signup():
	    if request.method == "POST":        
	        result = request.form          
	        email = result["email"]
	        password = result["pass"]
	        confirmpassword = result["confirmpass"]
	        name = result["name"]
	        try:
	        	if person["pass"] == person["confirmpass"]
	            auth.create_user_with_email_and_password(email, password)

	            user = auth.sign_in_with_email_and_password(email, password)

	            global person
	            person["is_logged_in"] = True
	            person["email"] = user["email"]
	            person["uid"] = user["localId"]
	            person["name"] = name

	            data = {"name": name, "email": email}
	            db.child("users").child(person["uid"]).set(data)

	            flash(f'Acccount successfully created!', 'success')
	            return redirect(url_for('home'))
	        except:

	            return redirect(url_for('signup'))
	

	    else:
	        if person["is_logged_in"] == True:
	        	flash(f'You have been logged in.', 'success')
	            return redirect(url_for('home'))
	        else:
	            return redirect(url_for('signup'))
	
     return render_template("signup.html")


if __name__ == "__main__":
	    app.run()

