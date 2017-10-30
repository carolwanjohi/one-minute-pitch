from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class LineForm(FlaskForm):
    '''
    Function to create a wtf form for creating a pitch
    '''
    line_content =  StringField('One Minute Pitch', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    '''
    Function to create a wtf form for creating a feedback on a pitch
    '''
    comment_content =  StringField('Comment', validators=[Required()])
    submit = SubmitField('Submit')
