import peewee
from models import Game

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.7 (from the example template)"


if __name__ == "__main__":
    # Only for debugging while developing
    try:
        Game.create_table()
    except peewee.OperationalError:
        print('Games table already exists!')

    app.run(host='0.0.0.0', debug=True, port=80)
