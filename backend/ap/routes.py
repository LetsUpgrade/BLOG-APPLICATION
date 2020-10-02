from flask import render_template, url_for, flash, redirect, request
from ap import app, db, bcrypt, mail
from ap.forms import SignUpForm, LoginForm, PostForm, RequestResetForm, ResetPasswordForm
from ap.models import User, Post, Setting
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message


@app.route("/")
@app.route("/home", methods = ['GET','POST'])
def home():
	posts = Post.query.order_by(Post.date.desc()).all()
	return render_template('base.html', title = 'Home', posts=posts)

@app.route("/post/<int:post_id>")
def inner_blog(post_id):
	return render_template('inner_blog.html', title = 'Blog')

@app.route("/settings", methods = ['GET','POST'])
@login_required
def settings():
	if(request.method=='POST'):
		name = request.form.get('name')
		designation = request.form.get('designation')
		bio = request.form.get('bio')
		image_file = request.form.get('image_file')
		changes = Setting(name=name, designation=designation, bio=bio, image_file=image_file)	
		db.session.add(changes)
		db.session.commit()
	return render_template('setting.html', title = 'Profile Settings')



@app.route("/create_blog", methods = ['GET','POST'])
@login_required
def create_blog():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(title = form.title.data, content = form.content.data, author = form.author.data)
		db.session.add(post)
		db.session.commit()
		flash('Your post has been created.', 'success')
		return redirect(url_for('home'))
	return render_template('create_blog.html', title = 'Create Blog', form=form)



@app.route("/signup", methods=['GET', 'POST'])
def signup():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = SignUpForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Your account has been created! You are now able to log in', 'success')
		return redirect(url_for('login'))
	return render_template('signup.html', title='Sign Up', form=form)
    	
    

@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')
	return render_template('login1.html', title='Login', form=form)	
    	
def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message('Password Reset Request', sender = 'noreply@demo.com', recipients = [user.email])
	msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token = token, _external = True)}

If you did not make this request them simply ignore this email and no changes will be made
'''
	mail.send(msg)

@app.route("/reset_password", methods = ['GET','POST'])
def reset_password():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RequestResetForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email = form.email.data).first()
		send_reset_email(user)
		flash('An email has been sent with instructions to reset your password.', 'info')
		return redirect(url_for('login'))
	return render_template('reset_password.html', title='Reset password', forms = form)

@app.route("/reset_password/<token>", methods = ['GET','POST'])
def reset_token(token):
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	user = User.veiry_reset_token(token)
	if user is None:
		flash('That is an invalid or expired token', 'warning')
		return redirect(url_for('reset_password'))
	form = ResetPasswordForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user.password = hashed_password
		db.session.commit()
		flash('Your password has been changed! You are now able to log in', 'success')
		return redirect(url_for('login'))
	return render_template('reset_token.html', title='Reset password', forms = form)

@app.route("/profile/<string:id>")
def profilefn(id):
    prof = User.query.filter_by(id=id).first()
    blog = Post.query.filter(Post.id).all()
    return render_template("profile.html", prof=prof, blog=blog)




	
		
	
	
		
		
		
			
			
			
		
			
		


		
			
			
			
		
			
	
