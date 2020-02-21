from PIL import Image, ImageDraw, ImageFont
import json
import os
def image(name):
  try:
    os.mkdir(name)
  except:
    print("already have the folder")
  tweets = []
  with open(name+'.json') as file:
    tweets = json.load(file)
  cnt = 0
  for i in tweets:
    u = i.encode(encoding='UTF-8',errors='strict')
    cnt += 1
    img = Image.new('RGB', (1000, 150), color = (73, 109, 137))
    d = ImageDraw.Draw(img)
    print(i)
    d.text((20,20), u, fill=(255,255,0))
    img.save(name+'/'+name+'{}.png'.format(cnt))