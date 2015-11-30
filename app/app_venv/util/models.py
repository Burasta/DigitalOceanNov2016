from . import db


class Tweet(db.Model):
    __tablename__ = 'tweets'

    tweet_id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String)

    def __repr__(self):
        return "<tweet(tweet='%s')>" % self.tweet


class User(db.Model):
    __tablename__ = 'users'

    userID = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String)
    userPassword = db.Column(db.String)
    userRole = db.Column(db.String)

    def __repr__(self):
        return "<userName(userName='%s')>" % self.userName

    def get_role(self):
        return "<userRole(userRole='%s')>" % self.userRole
