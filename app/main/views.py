from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Group,Line
from .forms import LineForm
from flask_login import login_required,current_user

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
    lines = Line.get_lines(id)
    title = f'{group.name} page'

    return render_template('group.html', title=title, group=group, lines=lines)

@main.route('/group/line/new/<int:id>', methods=['GET','POST'])
@login_required
def new_line(id):

    '''
    View new line route function that returns a page with a form to create a pitch for the specified category
    '''
    group = Group.query.filter_by(id=id).first()

    if group is None:
        abort(404)

    form = LineForm()

    if form.validate_on_submit():
        line_content = form.line_content.data
        new_line = Line( line_content=line_content, group=group, user=current_user)
        new_line.save_line()

        return redirect(url_for('.group', id=group.id ))

    title = 'New Pitch page'
    return render_template('new_line.html', title=title, line_form=form)


   

