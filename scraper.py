import re
import threading
import time
from twitter_scraper import get_tweets

text = ""
new_code = ""
old_code = "FREEXXXXX"


def mostRecentTweet():
    global text
    while True:
        start = time.time()
        for tweet in get_tweets("chipotletweets", pages=1):
            text = tweet["text"]
            print(text)
        end = time.time()
        print("Retrieved in: " + str(end - start) + " seconds!")


def getCode():
    global new_code
    words = text.split()
    for word in words:
        if "FREE" in word:
            new_code = word


def sendText():
    global old_code
    if new_code is not old_code:
        pass
    pass


t1 = threading.Thread(target=mostRecentTweet)
t2 = threading.Thread(target=sendText)

t1.start()
t2.start()

t1.join()
t2.join()
