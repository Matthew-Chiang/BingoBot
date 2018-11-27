import os
from flask import Flask, flash, request, redirect, url_for, session, render_template, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging

import continuous
# import startCheck
import threading

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')



UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def fileUpload():
    target=os.path.join(UPLOAD_FOLDER,'test_docs')
    if not os.path.isdir(target):
        os.mkdir(target)
    logger.info("welcome to upload")
    file = request.files['file']
    filename = secure_filename(file.filename)
    destination="/".join([target, filename])
    file.save(destination)
    session['uploadFilePath']=destination

    from tesseractocr import getStr
    mat = getStr(destination).splitlines()
    board = []
    for line in mat:
        board.append(line.split)

    if len(board) == 5 and len(board[0] == 5)
        startCheck.setBoard(board)

    logger.info("startedRecording")

    speech_thread = threading.Thread(target=continuous.main)
    speech_thread.start()


    # print("start")
    # startCheck.s()


    return jsonify(code=board)

@app.route('/startRecording', methods=['POST'])
def startRecording():
    logger.info("startedRecording")

    speech_thread = threading.Thread(target=continuous.main)
    speech_thread.start()

    # startCheck.main()



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",use_reloader=False)
