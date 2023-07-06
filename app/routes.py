from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Tushar'}
    posts = [
        {
            'author': {'username': 'Pankaj'},
            'body': 'Beautiful day in Pallakode'
        },
        {
            'author': {'username': 'Tripti'},
            'body': 'Drishyam movie was so thrilling!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)