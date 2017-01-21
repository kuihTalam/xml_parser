from urllib.request import urlopen
from xml.etree.ElementTree import parse
from twython import Twython
from random import randrange
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# Access twitter via Twython library
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# Download the RSS feed and parse it
#u = urlopen('http://feeds.reuters.com/reuters/businessNews')
#u = urlopen('http://planetpython.org/rss20.xml')
#u = urlopen('http://feeds.skynews.com/feeds/rss/technology.xml')
#u = urlopen('http://rss.nytimes.com/services/xml/rss/nyt/Business.xml')
#u = urlopen('http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml')
#u = urlopen('http://feeds.bbci.co.uk/news/business/rss.xml?edition=uk')
u = urlopen('http://feeds.theedgemarkets.com/theedgemarkets/mymarkets.rss')
doc = parse(u)

# Extract and output tags of interest
newsfeed = []
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    #date = item.findtext('pubDate')
    newsfeed.append(title)
    print(title)
    #print(date)
    print() 

twits = newsfeed[randrange(1,10)] # Randomly select one of the first 10 
twitter.update_status(status=twits) # Push it to twitter
print("Tweeted: %s" % twits)

