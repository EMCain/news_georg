import re

pattern = re.compile(r'average (?P<subject>\w+) (?P<verb>.*?)(?P<number>\d+)(?P<ending>.*?)[?.!,;-]')

result = {
  "source": {
      "id": "wired",
      "name": "Wired"
  },
  "author": "Zachary Karabell",
  "title": "Apple Abandons the Mass Market, as the iPhone Turns Luxury",
  "description": "The average iPhone sold for nearly $800 in the most recent quarter; if the price keeps climbing at that rate, the average price may soon top $1,000.",
  "url": "https://www.wired.com/story/apple-abandons-mass-market-as-iphone-turns-luxury/",
  "urlToImage": "https://media.wired.com/photos/5bdcb0f77c13dd315f171352/191:100/pass/Apple-1053344586.jpg",
  "publishedAt": "2018-11-03T12:00:00Z",
  "content": "Big companies attract big attention, and none quite as much as Apple. Its quarterly reports have become something of a collective soothsaying moment for stock markets and the tech industry, and so Thursdays report garnered its usual share of outsized attentio\u2026 [+5148 chars]"
}


georg_template = u'“{factoid}” factoid actualy just statistical error. average {subject} {verb}0{ending}. {subject} Georg, who lives in cave & {verb}10,000, is an outlier adn should not have been counted'

def correct(headline):
    match = pattern.search(headline)

    bounds = match.span()
    factoid = match.string[bounds[0]:bounds[1] - 1] # remove final punctuation
    print(georg_template.format(
        factoid=factoid,
        subject=match.group('subject'),
        verb=match.group('verb'),
    ending=match.group('ending')
))


# works:
correct(result.get("description"))

# doesn't work:
correct(u'Whiplash victims awarded average of \u20ac20,000 for injuries')

# ...kind of works
correct(u' In fact, according to the SparkScore tool from the Twitter marketing service SparkToro, an average tweet from her gets 3 times as many retweets and 10 times as many faves.')
# based on https://lifehacker.com/see-exactly-how-fake-your-twitter-followers-are-1829600902 but with numbers replaced by digits
