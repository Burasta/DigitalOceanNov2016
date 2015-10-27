from flask.ext.wtf import Form
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class TweetForm(Form):
    tweet_text = TextAreaField('Write your tweet here.', validators=[DataRequired()])
    submit = SubmitField('Submit')
