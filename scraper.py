import re
import threading
import time
from twitter_scraper import get_tweets

text = ""

def mostRecentTweet():
    global text
    while True:
        start = time.time()
        for tweet in get_tweets("chipotletweets", pages=1):
            text = tweet["text"]
            print(text)
        end = time.time()
        #print("Retrieved in: " + str(end - start) + " seconds!")

def printText():
    print(text)
    #time.sleep(0.5)

t1 = threading.Thread(target=mostRecentTweet)
t2 = threading.Thread(target=mostRecentTweet)
t3 = threading.Thread(target=mostRecentTweet)
t4 = threading.Thread(target=printText)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
