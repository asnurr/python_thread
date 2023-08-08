import cv2

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def show_frame(self):
        ret, frame = self.cap.read()

        if ret:
            return ret, frame
        else:
            return False, None

    def release(self):
        self.cap.release()
