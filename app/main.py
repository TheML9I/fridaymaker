import datetime
import json
import requests

import peewee
from flask import Flask

from models import Game

app = Flask(__name__)

APPS_LISTING_URI = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'
APP_INFO_URI = 'https://store.steampowered.com/api/appdetails?appids={appid}&cc={cc}}'
COUNTRY_CODE = 'by'


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


def get_app_info(appid):
    endpoint = APP_INFO_URI.format(appid=appid, cc=COUNTRY_CODE)
    response = requests.get(endpoint)
    if response.status_code != 200:
        return
    app_json = json.loads(response.text)[str(appid)]['data']
    company_data = {
        'appid': app_json['steam_appid'],
        'name': app_json['name'],
        'app_type': app_json['type'],
        'is_free': app_json['is_free'],
        'detailed_description': app_json['detailed_description'],
        'about_the_game': app_json['about_the_game'],
        'pc_requirements': app_json['pc_requirements'],
        'mac_requirements': app_json['mac_requirements'],
        'linux_requirements': app_json['linux_requirements'],
        'initial_price': app_json['price_overview']['initial'],
        'final_price': app_json['price_overview']['final'],
        'discount_percent': app_json['price_overview']['initial'],
        'price_currency': app_json['price_overview']['currency'],
        'windows_compatible': app_json['platforms']['windows'],
        'mac_compatible': app_json['platforms']['mac'],
        'linux_compatible': app_json['platforms']['linux'],
        'genres': app_json['categories'],
        'updated_at': datetime.datetime.now,
    }


if __name__ == "__main__":
    # Only for debugging while developing
    try:
        Game.create_table()
    except peewee.OperationalError:
        print('Games table already exists!')
    app.run(host='0.0.0.0', debug=True, port=80)
