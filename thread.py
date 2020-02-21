import threading
from queue import *
from gettweet import *
from texttoimage import *
from image2video import *


def thread():
    cnt = 0 
    while True:
        if q.empty():
            break
        work = q.get()
        cnt += 1
        print("working on {}th thread".format(cnt))
        get_all_tweets(work)
        image(work)
        video(work)
        q.task_done()


tweets = ["@BU_Tweets","@BUAthletics","@BUexperts"]
q = Queue()
for i in tweets:
    q.put(i)
num_threads = 3
threads = []
for i in range(num_threads):
    t = threading.Thread(target=thread)
    t.daemon = True
    threads.append(t)
    t.start()
q.join() 

