from app import app
from flask import render_template

@app.route("/")
@app.route("/home")
def home():
    user = {'username': 'Rashid'}
    posts = [
        {
            'author': 'Susan',
            'body' : 'Beautiful day in portland'            
        },
        {
            'author' : 'James',
            'body' : 'Plan yourself accordingly'
        }
    ]
    return 