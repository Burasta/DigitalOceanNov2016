from flask.ext.wtf import Form
from wtforms import TextAreaField, SubmitField, PasswordField, StringField
from wtforms.validators import DataRequired, EqualTo


class ChatLogin(Form):
    userName = StringField('Username', validators=[DataRequired()])
    userPassword = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


class ChatRegistration(Form):
    userName = StringField('Username', validators=[DataRequired()])
    userPassword = PasswordField('Password', validators=[DataRequired()])
    userPasswordConfirm = PasswordField('Confirm Password', validators=[EqualTo('userPassword')])
    submit = SubmitField('Submit')


class TweetForm(Form):
    tweet_text = TextAreaField('Write your tweet here.', validators=[DataRequired()])
    submit = SubmitField('Submit')
