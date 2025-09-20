import cv2
import mediapipe as mp
import numpy as np
from web_cam import Webcam


class SmartFaceMeshWebcam(Webcam):
    def __init__(self, camera_index=0, window_name="Smart FaceMesh", resize_dim=(640, 480), max_faces=5):
        super().__init__(camera_index, window_name)
        self.resize_dim = resize_dim

        # MediaPipe Face Mesh
        self.mp_face_mesh = mp.solutions.face_mesh
        self.mp_drawing = mp.solutions.drawing_utils
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=max_faces,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

        # Drawing specs
        self.drawing_spec = self.mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

        # Thresholds
        self.blink_threshold = 0.25
        self.mouth_threshold = 0.6

        # Landmark indices
        self.LEFT_EYE = [33, 160, 158, 133, 153, 144]
        self.RIGHT_EYE = [362, 385, 387, 263, 373, 380]
        self.MOUTH = [61, 81, 311, 291, 178, 402]

    def _aspect_ratio(self, landmarks, frame_shape, indices):
        h, w, _ = frame_shape
        points = np.array([[landmarks[i].x * w, landmarks[i].y * h] for i in indices])

        vertical = np.linalg.norm(points[1] - points[5]) + np.linalg.norm(points[2] - points[4])
        horizontal = np.linalg.norm(points[0] - points[3])
        ratio = vertical / (2.0 * horizontal + 1e-6)
        return ratio

    def extract_landmarks(self, landmarks):
        """Return flattened landmarks for ML model"""
        return np.array([[lm.x, lm.y, lm.z] for lm in landmarks.landmark]).flatten()

    def process_frame(self, frame):
        """Process a single frame, return frame + info list for all faces"""
        frame = cv2.resize(frame, self.resize_dim)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)
        all_faces_info = []

        if results.multi_face_landmarks:
            for landmarks in results.multi_face_landmarks:
                info = {"blink": False, "mouth_open": False, "landmarks": None}
                info["landmarks"] = self.extract_landmarks(landmarks)

                # EAR
                left_EAR = self._aspect_ratio(landmarks.landmark, frame.shape, self.LEFT_EYE)
                right_EAR = self._aspect_ratio(landmarks.landmark, frame.shape, self.RIGHT_EYE)
                avg_EAR = (left_EAR + right_EAR) / 2.0
                if avg_EAR < self.blink_threshold:
                    info["blink"] = True

                # MAR
                mar = self._aspect_ratio(landmarks.landmark, frame.shape, self.MOUTH)
                if mar > self.mouth_threshold:
                    info["mouth_open"] = True

                # Draw mesh
                self.mp_drawing.draw_landmarks(
                    frame, landmarks, self.mp_face_mesh.FACEMESH_TESSELATION,
                    self.mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                    self.mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=1)
                )

                all_faces_info.append(info)

        return frame, all_faces_info

    def show(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            frame, faces_info = self.process_frame(frame)

            # Display info for each face
            for idx, info in enumerate(faces_info):
                y_offset = 50 + idx * 50
                if info["blink"]:
                    cv2.putText(frame, f"Face {idx+1}: Blink", (30, y_offset),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                if info["mouth_open"]:
                    cv2.putText(frame, f"Face {idx+1}: Mouth Open", (30, y_offset + 25),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            cv2.imshow(self.window_name, frame)
            if cv2.waitKey(1) & 0xFF == 27:  # ESC
                break

        self.release()


if __name__ == "__main__":
    mesh_cam = SmartFaceMeshWebcam(max_faces=5)  # Detect up to 5 faces
    mesh_cam.show()


# ==============================
# 📌 Variable Reference (Docs) - mesh.py
# ==============================

# Inherited Variables (from Webcam)
# ---------------------------------
# self.cap          → OpenCV VideoCapture object (captures webcam frames)
# self.window_name  → Name of the OpenCV window used to display frames

# FaceMesh Variables
# ------------------
# self.mp_face_mesh → Reference to MediaPipe's FaceMesh solution
# self.mp_drawing   → MediaPipe drawing utilities (for rendering landmarks)
# self.face_mesh    → Initialized FaceMesh model with parameters:
#                       - max_num_faces (default: 1)
#                       - refine_landmarks (better detail on eyes/lips)
#                       - min_detection_confidence (default: 0.5)
#                       - min_tracking_confidence (default: 0.5)

# Frame Processing Variables
# --------------------------
# ret, frame        → Frame capture result and the actual webcam frame
# rgb_frame         → Frame converted from BGR (OpenCV) to RGB (for MediaPipe)
# results           → Output of FaceMesh processing (contains detected landmarks)
# landmarks         → Landmark points for a single detected face

# Methods
# -------
# show()            → Runs the webcam loop, applies FaceMesh, and displays output
# release()         → Releases webcam and closes OpenCV windows (inherited)
