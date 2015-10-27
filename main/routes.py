from . import app
from flask import render_template
from util.forms import TweetForm
from util.models import Tweet, db


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/tweets/', methods=["GET", "POST"])
def tweets():
    tweet = None
    form = TweetForm()
    if form.validate_on_submit():
        tweet = Tweet
        tweet.tweet = form.tweet_text.data
        tweet.tweet_id = None
        db.session.add(tweet)
        form.tweet_text.data = ''
    return render_template('tweets.html', form=form, tweet=tweet)
