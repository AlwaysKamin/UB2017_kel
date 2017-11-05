
from tkinter import *

# import cv2
# from blockDetection import blockDetection
class GUI:
  def __init__(self, master):
    frame = Frame(master)
    master.title("Apprentice")
    frame.pack()
    self.button = Button(frame,
                         text="Scan Block",
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
                          command=temp_one(1))
    self.button3.grid(row=1, column=0)

    self.button4 = Button(frame,
                          text="Choose Template 2",
                          width=15,
                          command=temp_one(2))
    self.button4.grid(row=2, column=0)

def temp_one(temp_choice):
    block_dem = [["x", "x", "x", "x"], ["x", "x", "x", "x"]]
    if temp_choice == 1:
        for i in range(len(block_dem)):
            for j in range(len(block_dem[i])):
                if j == 1:
                    block_dem[i][j] = 7
                print(block_dem)

    if temp_choice == 2:
        for i in range(len(block_dem)):
            for j in range(len(block_dem[i])):
                if j == 2:
                    block_dem[i][j] = 8
                print(block_dem)



def main():
    while True:
        # camera = blockDetection()
        # cameraFrame = camera.grabFrames()
        # camera.display(cameraFrame)
        root = Tk()
        root.title("Apprentice")
        root.geometry("350x200")
        app = GUI(root)
        root.mainloop()

        # # Used for an exit button for now
        # key = cv2.waitKey(1) & 0xFF
        # if key == ord("q"):
        #     camera.exit()
        #     break

if __name__ ==  "__main__":
    main()