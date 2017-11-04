import sys
import ctypes
from tkinter import *
#from sdl2 import*
import cv2
from blockDetection import blockDetection
class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame,
                         text="Scan Block",
                         command=quit)
    self.button.grid(row=0, column=0)
    self.button2 = Button(frame,
                         text="Display on Block",
                         command=quit)
    self.button2.grid(row=0, column=1)

def main():
    while True:
        camera = blockDetection()
        cameraFrame = camera.grabFrames()
        camera.display(cameraFrame)
        # root = Tk()
        # root.title("Apprentice")
        # root.geometry("900x800")
        # app = App(root)
        # root.mainloop()

        # Used for an exit button for now
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            camera.exit()
            break

if __name__ ==  "__main__":
    main()