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


class Item(db.Model):
    __tablename__ = 'items'

    itemID = db.Column(db.Integer, primary_key=True)
    itemName = db.Column(db.String)
    itemDescription = db.Column(db.String)
    itemImage = db.Column(db.String)
    itemShop = db.Column(db.Integer)

    def __repr__(self):
        return "{Item Name: %s" % self.itemName

    def get_description(self):
        return "<itemDescription(itemDescription='%s')>" % self.itemDescription

    def get_image(self):
        return "<itemImage(itemImage='%s')>" % self.itemImage

    def get_shop(self):
        return "<itemShop(itemShop='%s')>" % self.itemShop
