
from tkinter import *

import cv2
from blockDetection import blockDetection
from projection import projection
from template import template2x4

class GUI:
  def __init__(self, master):
    frame = Frame(master)
    master.title("Apprentice")
    frame.pack()

    self.button0 = Button(frame,
                          text="Recognize Block",
                          width=15,
                          command=lambda: cameraMechanics())
    self.button0.grid(row = 0, column = 0)
    self.button1 = Button(frame,
                          text="Choose Template 1",
                          width=15,
                          command=lambda: templateSelection(1))
    self.button1.grid(row=1, column=0)
    self.button2 = Button(frame,
                          text="Choose Template 2",
                          width=15,
                          command=lambda: templateSelection(2))
    self.button2.grid(row=2, column=0)
    self.button3 = Button(frame,
                          text="Choose Template 3",
                          width=15,
                          command=lambda: templateSelection(3))
    self.button3.grid(row=3, column=0)
    self.button4 = Button(frame,
                         text="Quit",
                         width=15,
                         command=quit)
    self.button4.grid(row=4, column=0)

def templateSelection(choice):
    newTemplate = template2x4()
    if choice == 1:
        newTemplate.template_one()
        renderer(newTemplate, 1)
    elif choice ==2:
        newTemplate.template_two()
        renderer(newTemplate, 2)
    elif choice == 3:
        newTemplate.template_three()
        renderer(newTemplate, 3)

def renderer(newTemplate2x4, classifier):
    print("Entering Renderer")
    testProjection = projection()
    numLines = len(newTemplate2x4.x)/2
    print(numLines)
    m = numLines
    n = numLines + 1
    while(numLines >= 0):
        print("inside while: " + str(numLines))
        m =+ 1
        n =+ 1
        if(classifier == 3):
            testProjection.drawCircle(newTemplate2x4)
        else:
            testProjection.draw(newTemplate2x4, m, n)
        numLines =- 1
    testProjection.display()


def cameraMechanics():
    print("Entering camera Mechanics")
    camera = blockDetection()
    cameraFrame = camera.grabFrames()
    cameraBW = camera.toBW(cameraFrame)
    cameraThres = camera.threshold(cameraBW)
    cameraDisplay = camera.locateAndDrawContours(cameraThres, cameraFrame)
    # camera.display(cameraThres)
    camera.display(cameraDisplay)

def main():
    while True:


        root = Tk()

        root.title("Apprentice")
        root.geometry("400x300")
        app = GUI(root)
        root.mainloop()

        # Used for an exit button for now
        # key = cv2.waitKey(1) & 0xFF
        # if key == ord("q"):
        #     camera.exit()
        #     break


if __name__ ==  "__main__":
    main()