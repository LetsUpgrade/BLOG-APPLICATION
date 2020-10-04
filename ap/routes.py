from flask import render_template, url_for, flash, redirect, request
from ap import app, db, bcrypt, mail
from ap.forms import SignUpForm, LoginForm, RequestResetForm, ResetPasswordForm
from ap.models import User, Post, Setting
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message


@app.route("/")
@app.route("/home", methods = ['GET','POST'])
def home():
	posts = Post.query.order_by(Post.date.desc())
	return render_template('base.html', title = 'Home', posts=posts, user=current_user)

@app.route("/post/<string:slug>")
@login_required
def inner_blog(slug):
	blog = Post.query.filter_by(slug = slug).first()
	s = slug.split('-')
	prof = User.query.filter_by(username= s[0]).first()
	return render_template('inner_blog.html', title = 'Blog', blog=blog, prof=prof)

@app.route("/settings/<string:id>", methods = ['GET','POST'])
@login_required
def settings(id):
	
	if(request.method=='POST'):
		User.name = request.form.get('name')
		User.designation = request.form.get('designation')
		User.about = request.form.get('about')
		User.image_file = request.form.get('image_file')
		# changes = User(name=name, designation=designation, about=about, image_file=image_file,id = current_user.id, username = current_user.username, email = current_user.email, password = current_user.password, post_no = current_user.post_no, following = current_user.following, followers = current_user.followers )
			
		
		db.session.commit()
	return render_template('setting.html', title = 'Profile Settings',user=current_user, id=id)



@app.route("/create_blog/<string:username>", methods = ['GET','POST'])
@login_required
def create_blog(username):
	
	
	if request.method == 'POST':
		title = request.form.get('title')
		content = request.form.get('content')
		img_file = request.form.get('img_file')
		title = title.replace(' ','-')
		slug = current_user.username + '-' + title
		post = Post(title = title, content = content, user_id = current_user.username, slug = slug)
		db.session.add(post)
		db.session.commit()
		flash('Your post has been created.', 'success')
		return redirect('/')
	return render_template('create_blog.html', title = 'Create Blog',username=username,user=current_user)



@app.route("/signup", methods=['GET', 'POST'])
def signup():
	# if current_user.is_authenticated:
	# 	return redirect(url_for('home'))
	form = SignUpForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		login_user(user, remember=form.remember.data)
		flash('Your account has been created! You are now able to log in', 'success')
		return redirect('/setting')
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
			
			
			# next_page = request.args.get('next')
			return redirect(url_for('home', current_user = current_user))
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')
	return render_template('login.html', title='Login', form=form)	
    	
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

@app.route("/profile/<string:username>")
@login_required
def profilefn(username):
	
	blog = Post.query.filter_by(user_id = current_user.username).all()
	return render_template("profile.html", blog=blog, user = current_user)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')




	
		
	
	
		
		
		
			
			
			
		
			
		


		
			
			
			
		
			
	
