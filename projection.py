import sys
from tkinter import Tk, Canvas, Frame, BOTH


class Render(Frame):
    def __init__(self):
        super().__init__()\

        self.init_ui()

    def init_ui(self):
        self.master.title("Lines")

        fileName = open("templates/firstReadInTest.block", "r")

        for line in fileName:
            if ('L' or 'H') in line:
                self.pack(fill=BOTH, expand=1)
                canvas = Canvas(self)
                canvas.create_line(0, 25, 400, 25)
                canvas.create_line(10, 2500, 50, 0)
                canvas.pack(fill=BOTH, expand=1)

root = Tk()
ex = Render()
root.attributes('-fullscreen', True)
root.mainloop()