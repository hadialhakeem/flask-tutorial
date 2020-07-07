from app import application
from flask import render_template


@application.route('/')
@application.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)
