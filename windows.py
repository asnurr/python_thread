import cv2
import time

class First:
    def __init__(self, webcam):
        self.webcam = webcam

    def show(self):
        while True:
            ret, frame = self.webcam.show_frame()

            cv2.imshow("First Window", frame)

            time.sleep(1)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.webcam.release()
        cv2.destroyAllWindows()


class Second:
    def __init__(self, webcam):
        self.webcam = webcam

    def show(self):
        while True:
            ret, frame = self.webcam.show_frame()

            cv2.imshow("Second Window", frame)

            time.sleep(1)  # 1 saniye bekle

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.webcam.release()
        cv2.destroyAllWindows()


class Third:
    def __init__(self, webcam):
        self.webcam = webcam

    def show(self):
        while True:
            ret, frame = self.webcam.show_frame()

            cv2.imshow("Third Window", frame)

            time.sleep(2)  # 2saniye bekle

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.webcam.release()
        cv2.destroyAllWindows()