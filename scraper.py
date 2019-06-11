import re
import time
from twitter_scraper import get_tweets

start = time.time()
for tweet in get_tweets("chipotletweets", pages=1):
    text = tweet["text"]
    print(text)
end = time.time()
print("Retrieved in: " + str(end - start) + " seconds!")
