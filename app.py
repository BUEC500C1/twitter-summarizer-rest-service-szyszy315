# app.py
import os
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
import subprocess
from moviepy.editor import VideoFileClip
import texttoimage
import image2video
import gettweet
import json
from flask_restful import Resource, Api

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, './')
app = Flask(__name__, template_folder=template_path, static_folder='static')
app.secret_key = "super secret key"
UPLOAD_FOLDER = '/uploads'
DOWNLOAD_FOLDER = './static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER


@app.route("/video")
def video():
    return '111'



@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        text = request.form['text']
        print(text,type(text))
        # if user does not select file, browser also
        # submit an empty part without filename
        if text == '':
            flash('No selected file')
            return redirect(request.url)
        gettweet.get_all_tweets(text)
        texttoimage.image(text)
        image2video.video(text)
        return redirect(url_for('download', filename=text))
    return render_template('template.html')



@app.route('/downloads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    file = filename + '.avi'
    if request.method == 'POST':
        return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename=file, as_attachment=True)
    return render_template('download.html', filename=filename)


@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)


if __name__ == "__main__":
    app.run()