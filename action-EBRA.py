#!/usr/bin/env python2
import feedparser
from hermes_python.hermes import Hermes
from datetime import datetime
from pytz import timezone

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

def parseRSS( rss_url ):
    return feedparser.parse( rss_url ) 
    
# Function grabs the rss feed headlines (titles) and returns them as a list
def getHeadlines( rss_url ):
    headlines = []
    
    feed = parseRSS( rss_url )
    for newsitem in feed['items']:
        headlines.append(newsitem['title'])
    
    return headlines

def intent_received(hermes, intent_message):

    if intent_message.intent.intent_name == 'DORNINEM:askNews':
		sentence = 'Il est '
		print(intent_message.intent.intent_name)
 
# Function to fetch the rss feed and return the parsed RSS
# A list to hold all headlines
allheadlines = []
 
# List of RSS feeds that we will fetch and combine
newsurls = {
    'DNA':           'https://www.dna.fr/rss'
#    'googlenews':       'https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US',
#    'yahoonews':        'http://news.yahoo.com/rss/'
}
 
# Iterate over the feed urls
for key,url in newsurls.items():
    # Call getHeadlines() and combine the returned headlines with allheadlines
    allheadlines.extend( getHeadlines( url ) )
 

# Iterate over the allheadlines list and print each headline
for hl in allheadlines:
    print(hl)
 
	print(sentence)

#	 summary = re.sub(r'\([^)]*\)|/[^/]*/', '', summary)



	hermes.publish_end_session(intent_message.session_id, sentence)
	


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
