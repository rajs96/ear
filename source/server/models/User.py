# import our initialized db
from . import db

#inherit from db.Model
#initialize UserModel class
class UserModel(db.Model):
	"""
	User Model
	"""
	# define name of table
	__tablename__ = 'users'

	# define the model for the User
	id = db.Column(db.Integer,primary_key=True)
	first_name = db.Column(db.String(128),nullable=False)
	last_name = db.Column(db.String(128), nullable=False)
	email = db.Column(db.String(128),nullable=False)

	# class constructor
	def __init__(self,data):
		"""
		Class constructor
		"""

		self.first_name = data.get("First Name")
		self.last_name = data.get("Last Name")
		self.email =data.get("Email")

	def save(self):
		db.session.add(self)
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()

