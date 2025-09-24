# Face Capture Module

This module is responsible for capturing facial data, which is the first step in the face recognition pipeline. It handles webcam integration, face detection, and the extraction of facial features (embeddings).

## Key Components:
- **`web_cam.py`**: A foundational class that provides a clean interface for accessing and controlling a webcam using OpenCV.
- **`face_capture.py`**: The core of this module. It uses the `web_cam` component and a face recognition library to process the video stream in real-time. It detects faces in each frame, draws a bounding box around them, and extracts the 128-d face embeddings that can be used for identification.

## Workflow:
1. The `Webcam` class initializes the camera.
2. `FaceRecognitionWebcam` (in `face_capture.py`) reads frames from the webcam.
3. For each frame, it detects all faces.
4. For each detected face, it computes a unique face embedding (a vector of 128 numbers).
5. The processed frame, with faces highlighted, is displayed to the user.