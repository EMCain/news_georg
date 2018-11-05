import requests, json
from os import environ
from dotenv import load_dotenv


load_dotenv()

base_params = {
    'apiKey': environ.get('API_KEY'),
    'language': 'en'
}

# top headlines
url = 'https://newsapi.org/v2/top-headlines?'
response = requests.get(url, params=base_params)
print(json.dumps(response.json(), indent=4))

# Apple query
url = 'https://newsapi.org/v2/everything?'
extra_params = {
    'q': 'Apple',
    'from': '2018-11-05',  # TODO get this as a datetime param
    'sortBy': 'popularity',
    'apiKey': environ.get('API_KEY')
}

response = requests.get(url, {**base_params, **extra_params})

print(json.dumps(response.json(), indent=4))  # sometimes results in character rendering weirdness



# Apple query
url = 'https://newsapi.org/v2/top-headlines?'
extra_params = {
    'q': 'average',
    'from': '2018-11-05',  # TODO get this as a datetime param
    'sortBy': 'popularity',
    'apiKey': environ.get('API_KEY')
}

response = requests.get(url, {**base_params, **extra_params})

print(json.dumps(response.json(), indent=4))  # sometimes results in character rendering weirdness
