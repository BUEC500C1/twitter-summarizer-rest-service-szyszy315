import pytest
import texttoimage
import image2video
import gettweet
import os
import subprocess
import json

def testcontentofjson(name):
  tweets = []
  jfile = name + ".json"
  with open(jfile,"r") as file:
    tweets = json.load(file)
  if len(tweets) != 20:
    print("error:didn't get enought tweets")
  for i in tweets:
    if isinstance(i, str) :
      continue
    else:
      print('error:cotent of json file  is wrong')
      return
  print("content of tweets is right")

def testifanyfilemiss(name):
  print (name + ".json file exists: "+ str(os.path.exists(name + '.json')))
  print (name + ".avi file exists: "+ str(os.path.exists(name + '.avi')))
  print(name + " folder exist: " + str(os.path.isdir(name)))

def testdurationofvideo(name) :
  result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", name + '.avi'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
  duration = int(result.stdout)
  print("duration = " + duration)
  if duration != 20:
    print("the duration of video wrong")
    return
  print("output video works")

def test():
  name = "@BU_Tweets"
  # gettweet.get_all_tweets(name)
  # texttoimage.image(name)
  # image2video.video(name)
  testcontentofjson(name)
  testifanyfilemiss(name)

if __name__ == '__main__':
  test()