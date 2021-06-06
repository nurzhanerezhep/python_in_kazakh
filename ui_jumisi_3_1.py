import random
import requests
from fastapi import FastAPI

app = FastAPI()

colleagues = ['Saken', 'Aliya', 'Shinbolat']

colleagues_db = {
    'saken': {
        'room_number': '504',
        'age': 28,
    }, 
    'aliya': {
        'room_number': '504',
        'age': 28,
    }    , 
    'shinbolat': {
        'room_number': '327',
        'age': 28,
    }
}
countries = ['Japan', 'Egypt', 'Iran', 'Turkish', 'France']

countries_db = {
    'Japan': {
        'population': '125 410 000',
        'city': 'Tokyo',
        'president': 'Haryhito'
    },
    'Egypt': {
        'population': '102 079 960	',
        'city': 'Kair',
        'president': 'Abdul-fattah As-sisi'
    },
    'Iran': {
        'population': '85 194 842',
        'city': 'Tegeran',
        'president': 'Hasan Ryhani'
    },
    'Turkish': {
        'population': '83 154 997',
        'city': 'Ankara',
        'president': 'Redjep Tayip Erdogan'
    },
    'France': {
        'population': '68 859 599',
        'city': 'Paris',
        'president': 'Emmanyel Makron'
    }
}


@app.get('/countries')
def countries():
    return countries_db

@app.get('/countries/{name}')
def countries(name):
    if name in countries_db:
        return countries_db[name]
    else:
        return 'Qate'

# quote
@app.get('/quotes/{name}')
def colleagues(name):
    response = requests.get('https://api.quotable.io/random')

    if response.status_code == 200:
        quote = response.json()
        result = 'Hi %s. You must read this text: %s' % (name.capitalize(), quote['content'])
        return result
    else:
        return 'Qate'
