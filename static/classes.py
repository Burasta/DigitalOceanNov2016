from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Tweet(Base):
    __tablename__ = 'tweets'

    tweet_id = Column(Integer, primary_key=True)
    tweet = Column(String)

    def __repr__(self):
        return "<tweet(tweet='%s')>" % self.tweet
