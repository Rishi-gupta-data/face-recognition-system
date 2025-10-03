import os
import cv2
import face_recognition

# Add project root to the Python path to allow importing the recognizer
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Backend.face_recognition.recognizer import FaceRecognizer

def search_for_face_in_videos(target_embedding, videos_directory):
    """
    Searches for a face matching the target_embedding in all videos within a directory.
    """
    matches = []
    recognizer = FaceRecognizer() # We need this to compare against all known faces, though not strictly for this search

    # Ensure the videos directory exists
    if not os.path.exists(videos_directory):
        print(f"Error: Directory not found at {videos_directory}")
        return []

    for video_filename in os.listdir(videos_directory):
        # Check for valid video file extensions
        if not video_filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            continue

        video_path = os.path.join(videos_directory, video_filename)
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            print(f"Warning: Could not open video file {video_path}")
            continue

        frame_count = 0
        fps = cap.get(cv2.CAP_PROP_FPS)
        # Process one frame per second (approx)
        frame_interval = int(fps) if fps > 0 else 1

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_count += 1
            if frame_count % frame_interval != 0:
                continue

            # Resize frame for faster processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Find all faces in the current frame
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            for face_encoding in face_encodings:
                # See if the face is a match for the target face
                results = face_recognition.compare_faces([target_embedding], face_encoding)
                if results[0]:
                    timestamp = frame_count / fps if fps > 0 else 0
                    match_data = {
                        "video_file": video_filename,
                        "timestamp_seconds": round(timestamp, 2),
                        "recognized_as": recognizer.recognize_face(face_encoding) # Get name if known
                    }
                    matches.append(match_data)
                    print(f"Match found in {video_filename} at {timestamp:.2f} seconds.")
        
        cap.release()

    return matches