
import os
import sys
from flask import Flask, request, jsonify
import face_recognition
import numpy as np
import cv2

# Add project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Backend.face_recognition.recognizer import FaceRecognizer
from Backend.Flask_Backend.video_search import search_for_face_in_videos

app = Flask(__name__)
recognizer = FaceRecognizer()

# Define the path to the recordings directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
VIDEOS_DIR = os.path.join(BASE_DIR, 'Data', 'recordings')

@app.route('/')
def hello_world():
    return 'Flask server is running. Use /recognize or /search_by_photo.'

@app.route('/recognize', methods=['POST'])
def recognize():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        filestr = file.read()
        npimg = np.frombuffer(filestr, np.uint8)
        image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
        rgb_image = image[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_image)
        face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

        recognized_names = []
        for face_encoding in face_encodings:
            name = recognizer.recognize_face(face_encoding)
            recognized_names.append(name)

        return jsonify({"recognized_names": recognized_names})

@app.route('/search_by_photo', methods=['POST'])
def search_by_photo():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        filestr = file.read()
        npimg = np.frombuffer(filestr, np.uint8)
        image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
        rgb_image = image[:, :, ::-1]

        # Find face embeddings in the uploaded photo
        face_locations = face_recognition.face_locations(rgb_image)
        face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

        if not face_encodings:
            return jsonify({"error": "No face found in the uploaded image"}), 400

        # Using the first face found in the image as the target
        target_embedding = face_encodings[0]

        # Call the search function
        matches = search_for_face_in_videos(target_embedding, VIDEOS_DIR)

        return jsonify({"matches": matches})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
