from flask import Flask, render_template
import sqlalchemy

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello')
def hello2():
    return render_template('test.html')


@app.route('/tweets')
def tweets():
    return render_template('tweets.html')

if __name__ == '__main__':
    app.run(debug=True)
