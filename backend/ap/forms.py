from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from ap.models import User


class SignUpForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Length(min=6, max=35)])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=6, max=20), EqualTo('password')])
	submit = SubmitField('Sign Up')


	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken. Please choose a different one.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email is taken. Please choose a different one.')
        
        
class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Length(min=6, max=35)])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class PostForm(FlaskForm):
	title = StringField('Title', validators = [DataRequired()])
	content = TextAreaField('content', validators = [DataRequired()])
	submit = SubmitField('Submit')
	

class RequestResetForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Length(min=6, max=35)])
	submit = StringField('Request Password Field')

	def validate_email(self, email):
		user = User.query.filter_by(email = email.data).first()
		if user is None:
			raise ValidationError('There is no account with that email. You must Register first.')

class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=6, max=20), EqualTo('password')])
	submit = StringField('Reset Password')


		