import threading
import time
from messenger import notify
from twitter import get_tweets

new_text = ""
old_text = ""
new_code = ""
old_code = ""


def most_recent_tweet():
    global new_text
    global old_text
    global new_code
    while True:
        start = time.time()
        for tweet in get_tweets("chipotletweets", pages=1):
            new_text = tweet["text"]
            print(new_text)
        end = time.time()
        if new_text != old_text:
            words = new_text.split(" ")
            for word in words:
                if "FREE" in word:
                    new_code = word
            old_text = new_text
        print("Retrieved in " + str(end - start)[:5] + " seconds!")


def send_text():
    global old_code
    while True:
        if new_code != old_code:
            notify(new_code)
            old_code = new_code


t1 = threading.Thread(target=most_recent_tweet)
t2 = threading.Thread(target=send_text)

t1.start()
t2.start()

t1.join()
t2.join()
