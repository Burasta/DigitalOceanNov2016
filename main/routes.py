from . import app
from flask import render_template
from util.forms import TweetForm
from util.models import Tweet, db
import json


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/tweets/', methods=["GET", "POST"])
def tweets():
    tweet = None
    form = TweetForm()
    if form.validate_on_submit():
        tweet = Tweet()
        tweet.tweet = form.tweet_text.data
        db.session.add(tweet)
        db.session.commit()
        form.tweet_text.data = ''
    return render_template('tweets.html', form=form, tweet=tweet)


@app.route('/get_tweets')
def get_tweets():
    tweet_query = Tweet.query.order_by(Tweet.tweet_id.desc()).limit(10)
    result = []
    for each in tweet_query:
        result.append(each.tweet)
    return json.dumps(result)
