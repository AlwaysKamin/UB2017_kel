
from tkinter import *

# import cv2
# from blockDetection import blockDetection
from projection import projection
from template import template2x4

class GUI:
  def __init__(self, master):
    frame = Frame(master)
    master.title("Apprentice")
    frame.pack()
    self.button = Button(frame,
                         text="Quit",
                         width=15,
                         command=quit)
    self.button.grid(row=0, column=1)
    self.button2 = Button(frame,
                         text="Display on Block",
                         width=15,
                         command=quit)
    self.button2.grid(row=0, column=2)
    self.button3 = Button(frame,
                          text="Choose Template 1",
                          width=15,
                          command=lambda: templateSelection(1))
    self.button3.grid(row=1, column=0)

    self.button4 = Button(frame,
                          text="Choose Template 2",
                          width=15,
                          command=lambda: templateSelection(2))
    self.button4.grid(row=2, column=0)
    self.button3 = Button(frame,
                          text="Display on Block",
                          width=15,
                          command=quit)

# def temp_one(temp_choice):
#     x = [0, 0, 0, 0]
#     y = [0, 0, 0, 0]
#     if temp_choice == 1:
#         # x1 = 175
#         # y1 = 100
#         # x2 = 2000
#         # y2 = 100
#         # x3 = 1000
#         # y3 = 100
#         # x4 = 1000
#         # y4 = 250
#         x = [175, 2000, 1000, 1000]
#         y = [100, 100, 100, 250]
#         print("Temp One Selected")
#
#
#     if temp_choice == 2:
#         x = [175, 2000, 1000, 1000]
#         y = [100, 100, 100, 250]
def templateSelection(choice):
    newTemplate = template2x4()
    if choice == 1:
        newTemplate.template_one()
        renderer(newTemplate)
    elif choice ==2:
        newTemplate.template_two()
        renderer(newTemplate)

def renderer(newTemplate2x4):
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
        testProjection.draw(newTemplate2x4, m, n)
        numLines =- 1
    testProjection.display()


# def cameraMechanics():
#     print("Entering camera Mechanics")
#     camera = blockDetection()
#     cameraFrame = camera.grabFrames()
#     cameraBW = camera.toBW(cameraFrame)
#     cameraThres = camera.threshold(cameraBW)
#     cameraDisplay = camera.locateAndDrawContours(cameraThres, cameraFrame)
#     # camera.display(cameraThres)
#     camera.display(cameraDisplay)

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