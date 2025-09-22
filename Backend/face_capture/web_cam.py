
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


# ==============================
# 📌 Variable Reference (Docs) - web_cam.py
# ==============================

# Webcam Variables
# ----------------
# self.cap          → OpenCV VideoCapture object (captures webcam frames)
# self.window_name  → Name of the OpenCV window used to display frames

# Methods
# -------
# release()         → Safely releases the webcam and closes OpenCV windows
