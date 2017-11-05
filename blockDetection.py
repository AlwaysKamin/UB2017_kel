from collections import deque
import numpy as np
import imutils
import cv2


class blockDetection():

    def grabFrames(self):
        image = cv2.imread("Pictures/testThreshold14.jpg")
        image = imutils.rotate(image, 3)
        image = image[60:240, 100:750]
        return image

    def display(self, frame):
        cv2.imshow("Test Frame", frame)

    def toBW(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.fastNlMeansDenoising(gray)
        return gray

    def threshold(self, frame):
        ret, th1 = cv2.threshold(frame, 35, 255, cv2.THRESH_BINARY)
        return th1

    def locateAndDrawContours(self, frame, firstFrame):
        (image2, contours, hierarchy) = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(firstFrame, contours, -1, (0, 255, 43), 3)
        return firstFrame

    def exit(self):
        self.camera.release()
        cv2.destroyAllWindows()
