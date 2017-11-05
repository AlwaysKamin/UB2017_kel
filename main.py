
from tkinter import *

# import cv2
# from blockDetection import blockDetection
from projection import projection

global x
global y

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
                         command=lambda: renderer(x, y))
    self.button2.grid(row=0, column=2)
    self.button3 = Button(frame,
                          text="Choose Template 1",
                          width=15,
                          command=lambda: temp_one(1))
    self.button3.grid(row=1, column=0)

    self.button4 = Button(frame,
                          text="Choose Template 2",
                          width=15,
                          command=lambda: temp_one(2))
    self.button4.grid(row=2, column=0)

def temp_one(temp_choice):
    if temp_choice == 1:
        # x1 = 175
        # y1 = 100
        # x2 = 2000
        # y2 = 100
        # x3 = 1000
        # y3 = 100
        # x4 = 1000
        # y4 = 250
        x = [175, 2000, 1000, 1000]
        y = [100, 100, 100, 250]
        print("Temp One Selected")


    if temp_choice == 2:
        x1 = 175
        y1 = 100
        x2 = 2000
        y2 = 100
        x3 = 1000
        y3 = 100
        x4 = 1000
        y4 = 250

def renderer(x, y):
    print("Entering Renderer")
    testProjection = projection()
    testProjection.draw(x, y)
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
        root.geometry("350x200")
        app = GUI(root)
        root.mainloop()

        # Used for an exit button for now
        # key = cv2.waitKey(1) & 0xFF
        # if key == ord("q"):
        #     camera.exit()
        #     break

if __name__ ==  "__main__":
    main()