import os
import subprocess
def video(name):
    filename = name + "/" + name + "%01d" + ".png"
    outputpath = './static/' + name + ".avi"
    try:
        f = open(outputpath)
    # Do something with the file
    except IOError:
        subprocess.call(['ffmpeg','-framerate', '0.33', '-i', filename, outputpath])
        return
    finally:
        f.close()
    os.remove(outputpath)
    subprocess.call(['ffmpeg','-framerate', '0.33', '-i', filename, outputpath])