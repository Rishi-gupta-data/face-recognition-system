import cv2
import os
import sys
import time
import face_recognition
import tkinter as tk
from tkinter import simpledialog

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Backend.face_capture.web_cam import Webcam
from Backend.face_recognition.recognizer import FaceRecognizer

class FaceRecognitionWebcam(Webcam):
    """
    Real-time face recognition and capture using face_recognition.
    - Detects faces
    - Extracts 128-d embeddings
    - Captures cropped faces for dataset building
    """

    def __init__(self, camera_index=0, window_name="Face Recognition", resize_factor=0.25, data_path='../../Data/raw'):
        super().__init__(camera_index, window_name)
        self.resize_factor = resize_factor
        self.data_path = data_path
        self.snapshots_path = '../../Data/snapshots'
        os.makedirs(self.data_path, exist_ok=True)
        os.makedirs(self.snapshots_path, exist_ok=True)

        # Initialize FaceRecognizer
        self.recognizer = FaceRecognizer()

        # State variables
        self.face_locations = []
        self.face_encodings = []
        self.capture_mode = False
        self.capture_name = None
        self.capture_count = 0
        self.capture_limit = 30
        self.capture_single_frame = False

        # Button parameters
        self.capture_button_pos = (10, 70)
        self.capture_button_size = (180, 40)
        self.photo_button_pos = (10, 120)
        self.photo_button_size = (180, 40)
        
        # Create window and set mouse callback
        cv2.namedWindow(self.window_name)
        cv2.setMouseCallback(self.window_name, self.mouse_callback)

    def _get_name_popup(self):
        """Creates a Tkinter popup to get the user's name."""
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        name = simpledialog.askstring("Input", "Enter person's name (no spaces):", parent=root)
        root.destroy()
        if name:
            return name.strip()
        return None

    def mouse_callback(self, event, x, y, flags, param):
        """Handles mouse click events for the buttons."""
        if event == cv2.EVENT_LBUTTONDOWN:
            # Check Start/Abort Capture button
            cbx, cby = self.capture_button_pos
            cbw, cbh = self.capture_button_size
            if cbx <= x <= cbx + cbw and cby <= y <= cby + cbh:
                if not self.capture_mode:
                    self.capture_name = self._get_name_popup()
                    if self.capture_name:
                        person_path = os.path.join(self.data_path, self.capture_name)
                        os.makedirs(person_path, exist_ok=True)
                        self.capture_count = 0
                        self.capture_mode = True
                        print(f"[*] Starting capture for '{self.capture_name}'")
                    else:
                        print("[!] Name cannot be empty.")
                else:
                    print(f"[*] Capture aborted for '{self.capture_name}'.")
                    self.capture_mode, self.capture_name = False, None
                return

            # Check Take Photo button
            pbx, pby = self.photo_button_pos
            pbw, pbh = self.photo_button_size
            if pbx <= x <= pbx + pbw and pby <= y <= pby + pbh:
                self.capture_single_frame = True

    def process_frame(self, frame):
        """Detects faces, extracts embeddings, draws bounding boxes and landmarks."""
        # Resize frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=self.resize_factor, fy=self.resize_factor)
        rgb_small_frame = small_frame[:, :, ::-1]

        self.face_locations = face_recognition.face_locations(rgb_small_frame)
        self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)
        face_landmarks_list = face_recognition.face_landmarks(rgb_small_frame, self.face_locations)

        for i in range(len(self.face_locations)):
            top, right, bottom, left = self.face_locations[i]
            face_encoding = self.face_encodings[i]
            face_landmarks = face_landmarks_list[i]
            recognized_name = self.recognizer.recognize_face(face_encoding)

            top, right, bottom, left = int(top / self.resize_factor), int(right / self.resize_factor), int(bottom / self.resize_factor), int(left / self.resize_factor)

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            cv2.putText(frame, recognized_name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)

            for facial_feature in face_landmarks.keys():
                for point in face_landmarks[facial_feature]:
                    x, y = int(point[0] / self.resize_factor), int(point[1] / self.resize_factor)
                    cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

        return frame

    def show(self):
        """Main webcam loop with face detection + capture logic."""
        print("[INFO] Starting webcam...")
        time.sleep(1.0)  # camera warm-up

        while True:
            ret, frame = self.cap.read()
            if not ret or frame is None:
                print("Warning: Failed to grab frame. Retrying...")
                time.sleep(0.1)
                continue  # don't break, just retry

            processed_frame = self.process_frame(frame)

            # --- HANDLE SNAPSHOT BUTTON ---
            if self.capture_single_frame:
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                filename = os.path.join(self.snapshots_path, f"snapshot_{timestamp}.jpg")
                cv2.imwrite(filename, frame)
                print(f"[*] Snapshot saved to {filename}")
                self.capture_single_frame = False

            # --- DRAW BUTTONS ---
            cbx, cby = self.capture_button_pos
            cbw, cbh = self.capture_button_size
            capture_text = "Abort Capture" if self.capture_mode else "Start Capture"
            capture_color = (0, 0, 255) if self.capture_mode else (0, 255, 0)
            cv2.rectangle(processed_frame, (cbx, cby), (cbx + cbw, cby + cbh), capture_color, cv2.FILLED)
            cv2.putText(processed_frame, capture_text, (cbx + 10, cby + 28),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            pbx, pby = self.photo_button_pos
            pbw, pbh = self.photo_button_size
            cv2.rectangle(processed_frame, (pbx, pby), (pbx + pbw, pby + pbh), (0, 200, 200), cv2.FILLED)
            cv2.putText(processed_frame, "Take Photo", (pbx + 30, pby + 28),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

            # --- CAPTURE LOGIC ---
            if self.capture_mode and self.capture_name:
                if self.face_locations and self.capture_count < self.capture_limit:
                    top, right, bottom, left = self.face_locations[0]
                    top_orig, right_orig, bottom_orig, left_orig = (
                        int(top / self.resize_factor),
                        int(right / self.resize_factor),
                        int(bottom / self.resize_factor),
                        int(left / self.resize_factor)
                    )
                    cropped_face = frame[top_orig:bottom_orig, left_orig:right_orig]

                    if cropped_face.size != 0:
                        img_name = f"{self.capture_name}_{self.capture_count + 1}.jpg"
                        img_path = os.path.join(self.data_path, self.capture_name, img_name)
                        cv2.imwrite(img_path, cropped_face)
                        if self.face_encodings:
                            self.recognizer.add_face(self.capture_name, self.face_encodings[0])
                        print(f"Captured {self.capture_count + 1}/{self.capture_limit}")
                        self.capture_count += 1
                        time.sleep(0.2)

                    if self.capture_count >= self.capture_limit:
                        print(f"[*] Capture complete for '{self.capture_name}'.")
                        self.recognizer.load_known_faces()
                        self.capture_mode, self.capture_name = False, None

                elif not self.face_locations:
                    cv2.putText(processed_frame, "No face detected!", (10, 180),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            # --- DISPLAY & EXIT ---
            cv2.putText(processed_frame, "Press 'q' to exit", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.imshow(self.window_name, processed_frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break

        self.release()


if __name__ == "__main__":
    FaceRecognitionWebcam().show()
