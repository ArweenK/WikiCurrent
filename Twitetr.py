import tweepy
import wikipedia
from bs4 import BeautifulSoup
import time
import requests

auth = tweepy.OAuth1UserHandler(
    "zrOo4WURsXzTYIragWlM3t1HA", "PFsDnfcvoRrjeOhwl02U0S31VYVQLiyi4ob0HcmQ6b4cp9uYlR",
    "1602818822557564929-jxrgAZXRgytpdVxFvwjfpeu0OwHP7J", "Q52fGQ2SzCs82vppaL1AjLwZrschZDNCZBLNMYwxjfgG6"

)
api = tweepy.API(auth)

# Picture of the cat
# media = api.media_upload("cat.png")

# Tweeting
# tweet = "Testing!! "
# post_result = api.update_status(status=tweet, media_ids=[media.media_id])

URL = "https://en.wikipedia.org/wiki/Portal:Current_events"

# def scrape_wiki_current_events():

# Fetch the webpage
response = requests.get(URL)
# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')
# Find the main content div
content_div = soup.find(div='mw-content-text')
# Find the most recent event
# event = content_div.find('li').text

headertxt = soup.find("div", class_="current-events-content description").findAll("li")

for li in headertxt:
    print(li.text)

# descriptiontxt = headertxt.soup.find_all("ul")
print(headertxt)

# Save the event to a file
with open('wikipedia_current_events.txt', 'w') as f:
    f.write(headertxt)
