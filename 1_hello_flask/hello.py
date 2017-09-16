from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_pyladies():
    return "Hello, pyLadies! I'm a Flask app"


if __name__ == '__main__':
    app.run('0.0.0.0', 7000)
