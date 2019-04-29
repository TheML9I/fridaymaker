import json
import requests

import peewee
from flask import Flask

from models import db, Game

app = Flask(__name__)

APPS_LISTING_URI = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'


@app.route("/")
def hello():
    return "Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.7 (from the example template)"


def get_games_listing():
    response = requests.get(APPS_LISTING_URI)
    if response.status_code == 200:
        steam_apps = json.loads(response.text)['applist']['apps']
        print(f'{len(steam_apps)} apps active in Steam.')
        for steam_app in steam_apps:
            Game.get_or_create(**steam_app)


if __name__ == "__main__":
    # Only for debugging while developing
    try:
        Game.create_table()
    except peewee.OperationalError:
        print('Games table already exists!')
    app.run(host='0.0.0.0', debug=True, port=80)
