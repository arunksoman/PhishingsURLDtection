from flask_user import UserMixin, UserManager
from Project import db, app
# from flask_admin.contrib.sqla import ModelView

# Define User data-model
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # User Authentication fields
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email_confirmed_at = db.Column(db.DateTime())
    # Relationships
    roles = db.relationship('Roles', secondary='user_roles')

# Define the Role data-model
class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

# Define the UserRoles association table
class UserRoles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete='CASCADE'))

user_manager = UserManager(app, db, Users)

class Whitelist_url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    white_url = db.Column(db.String(50), nullable=False, unique=True)

class Blacklist_url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    black_url = db.Column(db.String(50), nullable=False, unique=True)
