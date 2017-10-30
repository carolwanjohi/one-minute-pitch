from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class LineForm(FlaskForm):
    '''
    Function to create a wtf form for creating a pitch
    '''
    line_content =  StringField('One Minute Pitch', validators=[Required()])
    submit = SubmitField('Submit')
