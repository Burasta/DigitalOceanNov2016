from . import db


class Tweet(db.Model):
    __tablename__ = 'tweets'

    tweet_id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String)

    def __repr__(self):
        return "<tweet(tweet='%s')>" % self.tweet
