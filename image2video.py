import os
import subprocess
def video(name):
    filename = name + "/" + name + "%01d" + ".png"
    outputpath = name + ".avi"
    subprocess.call(['ffmpeg', '-framerate', '1', '-i', filename, outputpath])