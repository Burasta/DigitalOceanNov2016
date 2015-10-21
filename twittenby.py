from flask import Flask, render_template
import sqlalchemy
import apsw

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/tweets')
def tweets():
    return render_template('tweets.html')

if __name__ == '__main__':
    app.run(debug=True)


def sql_connect():
    engine = sqlalchemy.create_engine('C:/Users/Brandon-Camp/PycharmProjects/twittenby/twittenby.db')
    connection = engine.connect()
    result = connection.execute("SELECT * FROM tweets")
    return result
