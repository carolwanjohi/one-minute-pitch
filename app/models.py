from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    '''
    @login_manager.user_loader Passes in a user_id to this function
    Function queries the database and gets a user's id as a response
    '''
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    '''
    User class to define a user in the database
    '''

    # Name of the table
    __tablename__ = 'users'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)

    # username column for usernames
    username = db.Column(db.String(255))

    # email column for a user's email address
    email = db.Column(db.String(255), unique=True, index=True)

    # password_hash column for passwords
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f'User {self.username}'



class Group(db.Model):
    '''
    Group class to define the categories for pitches
    '''

    # Name of the table
    __tablename__ = 'groups'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)
    
    # name column for names of categories
    name = db.Column(db.String(255))

    def save_group(self):
        '''
        Function that saves a new category to the groups table
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_groups(cls):
        '''
        Function that queries the database and returns all the information from the groups table

        Returns:
            groups : all the information in the groups table
        '''

        groups = Group.query.all()

        return groups







        