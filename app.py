import requests
import logging
import json

from chalice import Chalice
from chalicelib import secrets

app = Chalice(app_name='gochefit-webhooks')
app.log.setLevel(logging.DEBUG)
app.debug = True

url = secrets.get_secret('travis_url')
token = 'token ' + secrets.get_secret('travis_token')
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Travis-API-Version': '3',
    'Authorization': token
}


@app.route('/build/master', methods=['GET','POST','PUT'], api_key_required=True)
def build_master():
    payload = {
        'request': {
            'branch': 'master'
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    r.raise_for_status()

    return 'Ok'


@app.route('/build/prod', methods=['GET','POST','PUT'], api_key_required=True)
def build_prod():
    payload = {
        'request': {
            'branch': 'prod'
        }
    }
    # r = requests.post(url, headers=headers, data=json.dumps(payload))
    # r.raise_for_status()

    return 'Ok'
