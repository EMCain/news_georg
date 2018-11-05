import re, requests
from os import environ
from dotenv import load_dotenv


load_dotenv()

pattern = re.compile(r'average (?P<subject>\w+) (?P<verb>.*?)(?P<number>\d+)(?P<ending>.*?)[?.!,;-]')

georg_template = u'“{factoid}” factoid actualy just statistical error. average {subject} {verb}0{ending}. {subject} Georg, who lives in cave & {verb}10,000, is an outlier adn should not have been counted'

# average query
url = 'https://newsapi.org/v2/top-headlines?'

base_params = {
    'apiKey': environ.get('API_KEY'),
    'language': 'en'
}

extra_params = {
    'q': 'average',
    'from': '2018-10-05',  # TODO get this as a datetime param
    'sortBy': 'popularity',
    'apiKey': environ.get('API_KEY')
}


def get_match(result):
    for key in ['title', 'description', 'content']:
        headline = result.get(key)
        match = pattern.search(headline)
        if match is not None:
            return match
    # see if it's in the body
    resp = requests.get(result['url'])
    if resp.status_code == 200:
        return pattern.search(resp.body()) or None


def correct(match):
    bounds = match.span()
    factoid = match.string[bounds[0]:bounds[1] - 1] # remove final punctuation
    print(georg_template.format(
        factoid=factoid,
        subject=match.group('subject'),
        verb=match.group('verb'),
    ending=match.group('ending')
))

results = requests.get(url, {**base_params, **extra_params})
yes, no = 0, 0
for result in results.json().get('articles'):
    try:
        print(correct(get_match(result)))
        yes += 1
    except:
        no += 1

print(yes, no)
