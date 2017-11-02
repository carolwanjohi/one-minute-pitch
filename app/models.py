from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from sqlalchemy.sql import func

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
    email = db.Column(db.String(255), unique = True, index = True)

    # password_hash column for passwords
    password_hash = db.Column(db.String(255))

    # relationship between user and line class
    lines = db.relationship('Line', backref='user', lazy='dynamic')

    # relationship between user and comment class
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    # relationship between line and comment class
    votes = db.relationship('Vote', backref='user', lazy='dynamic')

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

    # relationship between group and line class
    lines = db.relationship('Line', backref='group', lazy='dynamic')

    def save_group(self):
        '''
        Function that saves a new category to the groups table
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_groups(cls):
        '''
        Function that queries the Groups Table in the database and returns all the information from the Groups Table

        Returns:
            groups : all the information in the groups table
        '''

        groups = Group.query.all()

        return groups


class Line(db.Model):
    '''
    Line class to define the pitches
    '''

    # Name of the table
    __tablename__ = 'lines'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)

    # line_content column for the one minute pitch a user writes
    line_content = db.Column(db.String(200))

    # group_id column for linking a line to a specific group
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id") )

    # user_id column for linking a line to a specific group
    user_id = db.Column(db.Integer, db.ForeignKey("users.id") )

    # relationship between line and comment class
    comments = db.relationship('Comment', backref='line', lazy='dynamic')

    # relationship between line and comment class
    votes = db.relationship('Vote', backref='line', lazy='dynamic')

    def save_line(self):
        '''
        Function that saves a new pitch to the lines table
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_lines(cls,group_id):
        '''
        Function that queries the Lines Table in the database and returns only information with the specified group id

        Args:
            group_id : specific group_id

        Returns:
            lines : all the information for lines with the specific group id 
        '''
        lines = Line.query.order_by(Line.id.desc()).filter_by(group_id=group_id).all()

        return lines

class Comment(db.Model):
    '''
    Comment class to define the feedback from users
    '''

    # Name of the table
    __tablename__ = 'comments'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)

    # comment_content for the feedback a user gives toa pitch
    comment_content = db.Column(db.String)

    # line_id column for linking a line to a specific line
    line_id = db.Column(db.Integer, db.ForeignKey("lines.id") )

    # user_id column for linking a line to a specific group
    user_id = db.Column(db.Integer, db.ForeignKey("users.id") )

    def save_comment(self):
        '''
        Function that saves a new comment given as feedback to a pitch
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,line_id):
        '''
        Function that queries the Comments Table in the database and returns only information with the specified line id

        Args:
            line_id : specific line_id

        Returns:
            comments : all the information for comments with the specific line id 
        '''
        comments = Comment.query.filter_by(line_id=line_id).all()

        return comments

class Vote(db.Model):
    '''
    Vote class to difine votes for a pitch
    '''

    # Name of the table
    __tablename__ = 'votes'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)

    # user_id column for linking a line to a specific group
    user_id = db.Column(db.Integer, db.ForeignKey("users.id") )

    # line_id column for linking a line to a specific line
    line_id = db.Column(db.Integer, db.ForeignKey("lines.id") )

    # vote_number column for the votes for a pitch by a user
    vote_number =  db.Column(db.Integer)

    def save_vote(self):
        '''
        Function that saves a new vote given to a pitch by a user
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def num_vote(cls,line_id):
        '''
        Function that queries the Votes table in the databse if it has a vote with the specified user_id and line_id and returns counts them

        Args:
            user_id : specific user_id 
            line_id : specific line_id

        .filter_by(user_id=user_id)

        .(func.sum(Vote.vote_number))

        found_votes = Vote.query.filter(user_id==user_id,line_id==line_id).with_entities(Vote.vote_number).value(Vote.vote_number)

        found_votes = Vote.query.filter(user_id==user_id,line_id==line_id).with_entities(Vote.vote_number).count()
        '''
        found_votes = db.session.query(func.sum(Vote.vote_number))
        found_votes = found_votes.filter_by(line_id=line_id).group_by(Vote.line_id)
        votes_list = sum([i[0] for i in found_votes.all()])
        # total_votes = sum(i for i in found_votes.all())
        # for _res in found_votes.all():
        #     total_votes = sum(_res)
        #     return total_votes

        
        # count = 0

        
        # for vote in range(found_votes):
        #     count += vote
        # for i in found_votes:
        #     result = count + i.value()
        #     return result
        return votes_list











        