
from tkinter import *

import cv2
from blockDetection import blockDetection
class GUI:
  def __init__(self, master):
    frame = Frame(master)
    master.title("Apprentice")
    frame.pack()
    self.button = Button(frame,
                         text="Scan Block",
                         command=quit)
    self.button.grid(row=0, column=0)
    self.button2 = Button(frame,
                         text="Display on Block",
                         command=quit)
    self.button2.grid(row=0, column=1)
    self.button3 = Button(frame,
                          text="Choose Template 1",
                          command=temp_one)
    self.button3.grid(row=1, column=0)

def temp_one():
    block_dem = "firstReadInTest.block"
    for i in range(len(block_dem)):
        for j in range(len(block_dem[i])):
            if j > 0 and j < 3:
                block_dem[i][j] = 7
            print(block_dem)

def main():
    while True:
        camera = blockDetection()
        cameraFrame = camera.grabFrames()
        camera.display(cameraFrame)
        root = Tk()
        root.title("Apprentice")
        root.geometry("500x400")
        app = GUI(root)
        root.mainloop()

        # Used for an exit button for now
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            camera.exit()
            break

if __name__ ==  "__main__":
    main()