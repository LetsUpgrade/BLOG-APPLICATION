from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serialzer
from ap import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20), unique = True, nullable = False)
	designation = db.Column(db.String(50), nullable = False)
	email = db.Column(db.String(60), unique = True, nullable = False)
	image_file = db.Column(db.String(50), nullable = False, default = 'default.jpg')
	about = db.Column(db.String(120), nullable = True)
	password = db.Column(db.String(60), nullable = False)
	post_no = db.Column(db.Integer, default=0)
	followers = db.Column(db.Integer, default=0)
	following = db.Column(db.Integer, default=0)

	def get_reset_token(self, expires_seconds=1800):
		s = Serialzer(app.config['SECRET_KEY'], expires_sec)
		return s.dumps({'user_id': self.id}).decode('utf-8')

	@staticmethod
	def verify_reset_token(token):
		s = Serialzer(app.config['SECRET_KEY'])
		try:
			user_id = s.loads(token)['user_id']
		except:
			return None
		return User.query.get(user_id)

	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(120), nullable = False)
	date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
	content = db.Column(db.Text, nullable = False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
	image_file = db.Column(db.String(50), nullable = False, default = 'default.jpg')

	def __repr__(self):
		return f"Post('{self.title}','{self.date}','{self.user_id}')"

class Setting(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(120), nullable = False)
	designation = db.Column(db.String(120), nullable = False)
	bio = db.Column(db.String(120), nullable = False)
	image_file = db.Column(db.String(50), nullable = False, default = 'default.jpg')

	def __repr__(self):
		return f"Setting('{self.name}','{self.designation}','{self.bio}','{self.image_file}')"