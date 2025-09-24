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
 48 changes: 48 additions & 0 deletions48  
Backend/face_capture/web_cam.py
Original file line number	Diff line number	Diff line change
@@ -0,0 +1,48 @@

import cv2

class Webcam:
    def __init__(self, camera_index=0, window_name="Webcam"):
        self.camera_index = camera_index
        self.window_name = window_name
        self.cap = cv2.VideoCapture(self.camera_index)

        if not self.cap.isOpened():
            raise Exception(f"Cannot open camera {self.camera_index}")

    def show(self):
        """Open webcam and display frames until ESC is pressed"""
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            cv2.imshow(self.window_name, frame)

            # Exit on ESC
            if cv2.waitKey(1) & 0xFF == 27:
                break

        self.release()

    def capture_frame(self, filename="capture.jpg"):
        """Capture a single frame and save as image"""
        ret, frame = self.cap.read()
        if ret:
            cv2.imwrite(filename, frame)
            print(f"Frame saved as {filename}")
        else:
            print("Failed to capture frame")

    def release(self):
        """Release camera and close windows"""
        self.cap.release()
        cv2.destroyAllWindows()


# Example usage
if __name__ == "__main__":
    webcam = Webcam()   # default camera 0
    webcam.show()       # opens webcam window
    # webcam.capture_frame("test.jpg")  # capture single frame