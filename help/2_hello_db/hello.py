from flask import Flask
from sqlalchemy import create_engine


app = Flask(__name__)


@app.route('/')
def hello_pyladies():
    return "Hello, pyLadies! I'm a Flask app"


@app.route('/db')
def hello_db():
    try:
        db = create_engine('postgresql://postgres:postgres@db:5432/postgres')
        result = db.execute('SELECT 1').first()
        if result and result[0] == 1:
            return 'Connected to the database \\o/'
    except Exception:
        return 'Cannot connect to the database :('


if __name__ == '__main__':
    app.run('0.0.0.0', 7000)
