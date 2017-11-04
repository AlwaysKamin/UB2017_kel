from collections import deque
import numpy as np
import imutils
import cv2


class blockDetection():
    camera = cv2.VideoCapture(1)

    def grabFrames(self):
        (grabbed, frame) = self.camera.read()
        # frame = imutils.resize(frame, width=600, height=600)
        return frame

    def display(self, frame):
        cv2.imshow("Test Frame", frame)

    def exit(self):
        self.camera.release()
        cv2.destroyAllWindows()
