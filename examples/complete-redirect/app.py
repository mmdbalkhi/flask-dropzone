# -*- coding: utf-8 -*-
import os

from flask import Flask, render_template, request
from flask_dropzone import Dropzone

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_INPUT_NAME='photo',
    DROPZONE_MAX_FILES=30,
    DROPZONE_REDIRECT_VIEW='completed'  # set redirect view
)

dropzone = Dropzone(app)


@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('photo')
        f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return render_template('index.html')


@app.route('/completed')
def completed():
    return '<h1>The Redirected Page</h1><p>Upload completed.</p>'


if __name__ == '__main__':
    app.run(debug=True)
