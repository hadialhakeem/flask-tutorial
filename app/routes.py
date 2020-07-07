from flask import render_template
from app import application
from app.forms import LoginForm


@application.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


@application.route('/')
@application.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)