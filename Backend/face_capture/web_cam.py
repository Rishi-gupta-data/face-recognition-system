import cv2

class Webcam:
    """
    A class to provide a clean interface for webcam operations using OpenCV.

    This class handles the initialization, frame capture, display, and release of a webcam feed.
    It is designed to be a reusable component for any application requiring webcam input.
    """
    def __init__(self, camera_index=0, window_name="Webcam"):
        """
        Initializes the Webcam object.

        Args:
            camera_index (int): The index of the camera to use (default is 0).
            window_name (str): The name of the window where the webcam feed will be displayed.
        """
        self.camera_index = camera_index
        self.window_name = window_name
        # Use cv2.CAP_DSHOW for better compatibility on Windows
        self.cap = cv2.VideoCapture(self.camera_index, cv2.CAP_DSHOW)

        # If the default camera is not opened, try to find one
        if not self.cap.isOpened():
            print(f"---[INFO] Camera index {self.camera_index} failed. Trying other indices...")
            for i in range(5): # Try indices 0 through 4
                if i == self.camera_index: continue
                cap_test = cv2.VideoCapture(i, cv2.CAP_DSHOW)
                if cap_test.isOpened():
                    print(f"---[INFO] Successfully opened camera at index {i}.")
                    self.camera_index = i
                    self.cap = cap_test
                    break
            else:
                self.cap = None # Explicitly set to None if no camera is found

        if self.cap is None or not self.cap.isOpened():
            raise Exception("Could not open any camera. Please check connection and drivers.")

    def show(self):
        """Open webcam and display frames until ESC is pressed."""
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
        """
        Capture a single frame and save it as an image file.

        Args:
            filename (str): The name of the file to save the captured frame as.
        """
        ret, frame = self.cap.read()
        if ret:
            cv2.imwrite(filename, frame)
            print(f"Frame saved as {filename}")
        else:
            print("Failed to capture frame")

    def release(self):
        """Release the camera and destroy all OpenCV windows."""
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()


# Example usage
if __name__ == "__main__":
    try:
        webcam = Webcam()   # default camera 0
        webcam.show()       # opens webcam window
    except Exception as e:
        print(e)