from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Group

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    groups = Group.get_groups()

    return render_template('index.html', title = title, groups=groups )

@main.route('/group/<int:id>')
def group(id):

    '''
    View group route function that returns a list of pitches in the route and allows a user to create a pitch for the selected route
    '''
    group = Group.query.get(id)
    title = f'{group.name} page'

    return render_template('group.html', title=title, group=group)


   

