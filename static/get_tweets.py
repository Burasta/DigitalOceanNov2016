from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Tweet(Base):
    __tablename__ = 'tweets'

    tweet_id = Column(Integer, primary_key=True)
    tweet = Column(String)

    def __repr__(self):
        return "<tweet(tweet='%s')>" % self.tweet

engine = create_engine('sqlite:///C:/Users/Brandon-Camp/PycharmProjects/twittenby/tweets.db')
Session = sessionmaker(bind=engine)
session = Session()

for instance in session.query(Tweet).order_by(Tweet.tweet_id.desc()):
    print instance.tweet

# with engine.connect() as connection:
#     result = connection.execute("SELECT tweet FROM tweets ORDER BY tweet_id DESC")
#     derp = {i: row['tweet'] for i, row in enumerate(result)}
#     print derp
