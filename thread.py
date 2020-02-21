import threading
from queue import *
from gettweet import *
from texttoimage import *
from image2video import *


def main(tweets):
    def thread():
        while True:
            if q.empty():
                break
            work = q.get()
            print('='*30)
            print("working on {} thread".format(work))
            get_all_tweets(work)
            image(work)
            video(work)
            print('='*30)
            print("{} thread done".format(work))
            q.task_done()
        print('all works done')
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

if __name__ == '__main__':
    tweets = ["@BU_Tweets","@BUAthletics","@BUexperts"]
    main(tweets)

