from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Tweet(Base):
    __tablename__ = 'tweets'

    tweet_id = Column(Integer, primary_key=True)
    tweet = Column(String)

    def __repr__(self):
        return "<tweet(tweet='%s')>" % self.tweet


class User(Base):
    __tablename__ = 'users'

    userID = Column(Integer, primary_key=True)
    userName = Column(String)
    userPassword = Column(String)
    userRole = Column(String)

    def __repr__(self):
        return "<userName(userName='%s')>" % self.userName

    def get_role(self):
        return "<userRole(userRole='%s')>" % self.userRole


class Item(Base):
    __tablename__ = 'items'

    itemID = Column(Integer, primary_key=True)
    itemName = Column(String)
    itemDescription = Column(String)
    itemImage = Column(String)
    itemShop = Column(Integer)

    def __repr__(self):
        return "<itemName(itemName='%s')>" % self.itemName

    def get_description(self):
        return "<itemDescription(itemDescription='%s')>" % self.itemDescription

    def get_image(self):
        return "<itemImage(itemImage='%s')>" % self.itemImage

    def get_shop(self):
        return "<itemShop(itemShop='%s')>" % self.itemShop
