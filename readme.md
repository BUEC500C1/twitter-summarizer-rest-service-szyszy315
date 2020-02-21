# HW4:  Individual Exercise:  FFmpeg
## run the code
### requirements
clone this repository
```
git clone https://github.com/BUEC500C1/video-szyszy315.git
```
Install all requirements by running
```
pip3 install -r requirements.txt
```
### run the code
```
python thread.py
```
Twitter text will be stored in json file. The image generated with tweets will be stored in folders with the same name as the twitter id. The output video will be in the root directory.<br>

## Main Exercise:  Using the twitter feed, construct a daily video summarizing a twitter handle day
First use tweepy to get the full text of twitter.
### Convert text into an image in a frame
Use PIL.ImageDraw to convert text to images.
### Do a sequence of all texts and images in chronological order.
Ffmpeg have function to generate video from images.
### Display each video frame for 3 seconds
Set -framerate 1/3 to display each video frame for 3 seconds.
```
    subprocess.call(['ffmpeg', '-framerate', '0.33', '-i', filename, outputpath])
```
## Multiprocessing vs Threading Python
Both processes and threads are independent sequences of execution. The typical difference is that threads (of the same process) run in a shared memory space, while processes run in separate memory spaces.

## Establish a processing criteria:
### How many API calls you can handle simultaneously and why?
Twitter API is the only api used in this project. In the thread.py i have 3 thread using twitter api simultaneously. 
### For example, run different API calls at the same time?
It is possible to run different api calls at the same times but in this case just 1 needed. 
### Split the processing of an API into multiple threads?
The processing of the api isn't splited into multiple threads. I just call the api in different threads simutaneously.
## track the thread
When the thread start working the name of the thread will be printed and you can learn from the image 3 threads start simutaneously.<br>
When a thread done it will show how many thread are still working<br>
When the work are all done it will print all works done.<br>
![image](https://github.com/BUEC500C1/video-szyszy315/blob/master/ec500hw4.png)
![image](https://github.com/BUEC500C1/video-szyszy315/blob/master/threadtrack.png)
