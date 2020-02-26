import pytest
import texttoimage
import image2video
import gettweet
import os
import json
from subprocess import  check_output, CalledProcessError, STDOUT 
import keys
# test the content of json file
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

# test if all neccessary file succesfully created
def testifanyfilemiss(name):
  print (name + ".json file exists: "+ str(os.path.exists(name + '.json')))
  print (name + ".avi file exists: "+ str(os.path.exists(name + '.avi')))
  print(name + " folder exist: " + str(os.path.isdir(name)))

# test the lenght of input video
def testdurationofvideo(name) :
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
    print("the duration of video wrong")
    return
  print("video successfully generated")

def test():
  name = "@BU_Tweets"
  if len(keys.CONSUMER_KEY) > 3 :
    # run the tested functions
    gettweet.get_all_tweets(name)
    texttoimage.image(name)
    image2video.video(name)
  #start the test
  testcontentofjson(name)
  testifanyfilemiss(name)
  testdurationofvideo(name)

if __name__ == '__main__':
  test()
