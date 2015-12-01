from . import app
from flask import render_template, redirect
from util.forms import TweetForm, ChatRegistration
from util.models import Tweet, db, User
import json


@app.route('/')
def welcome():
    return render_template('home.html')


@app.route('/chat/')
def chat():
    return redirect('http://www.appletarsenal.com/chat/')


@app.route('/helpme/')
def hello_world():
    return render_template('home.html')


@app.route('/tweets/', methods=["GET", "POST"])
def registration():
    user = None
    form = ChatRegistration()
    if form.validate_on_submit():
        user = User()
        user.userName = form.userName.data
        user.userPassword = form.userPasswordConfirm.data
        db.session.add(user)
        db.session.commit()
        form.userPasswordConfirm.data = ''
        form.userPassword.data = ''
        form.userName.data = ''
    return render_template('tweets.html', form=form, user=user)


@app.route('/get_tweets')
def get_tweets():
    tweet_query = Tweet.query.order_by(Tweet.tweet_id.desc()).limit(10)
    result = []
    for each in tweet_query:
        result.append(each.tweet)
    return json.dumps(result)
