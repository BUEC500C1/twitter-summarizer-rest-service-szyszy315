import pytest
import texttoimage
import image2video
import gettweet
import os
import json
from subprocess import  check_output, CalledProcessError, STDOUT 
import keys
# test the content of json file
def contentofjson(name):
  tweets = []
  jfile = name + ".json"
  with open(jfile,"r") as file:
    tweets = json.load(file)
  if len(tweets) != 20:
    return ("error:didn't get enought tweets")
  for i in tweets:
    if isinstance(i, str) :
      continue
    else:
      return ('error:cotent of json file  is wrong')
  return ("content of tweets is right")

# test if all neccessary file succesfully created
def ifanyfilemiss(name):
  print (name + ".avi file exists: "+ str(os.path.exists(name + '.avi')))
  print(name + " folder exist: " + str(os.path.isdir(name)))
  return (name + ".json file exists: "+ str(os.path.exists(name + '.json')))

# test the lenght of input video
def durationofvideo(name) :
  filename = name + ".avi"
  command = [
      'ffprobe', 
      '-v', 
      'error', 
      '-show_entries', 
      'format=duration', 
      '-of', 
      'default=noprint_wrappers=1:nokey=1', 
      filename
    ]
  try:
    output = check_output( command, stderr=STDOUT ).decode()
  except CalledProcessError as e:
    output = e.output.decode()
  duration = float(output)
  if int(duration) != 60:
    return ("the duration of video wrong")  
  return("video successfully generated")

def test_video():
  name = "@BU_Tweets"
  if (len(keys.CONSUMER_KEY) > 3) :
    # run the tested functions
    gettweet.get_all_tweets(name)
    texttoimage.image(name)
    image2video.video(name)
  #start the test
  assert contentofjson(name) == "content of tweets is right"
  assert ifanyfilemiss(name) == name + ".json file exists: True"
  assert durationofvideo(name) == "video successfully generated"
