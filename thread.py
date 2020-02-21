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
            print('='*97)
            print("working on {} thread".format(work))
            print()
            get_all_tweets(work)
            image(work)
            video(work)
            print('='*60)
            print("{} thread done".format(work))
            q.task_done()
            print('now {} threads are running, totally {} threads'.format(threading.activeCount()-2,len(tweets)))
            print('='*60)
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
    print('all works done')

if __name__ == '__main__':
    tweets = ["@BU_Tweets","@BUAthletics","@BUexperts"]
    main(tweets)

