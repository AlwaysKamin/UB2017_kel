from tkinter import Tk, Canvas, Frame, BOTH
import main

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
                canvas.create_line(main.x1, main.y1, main.x2, main.y2, width=10.0, fill="red")
                canvas.create_line(main.x3, main.y3, main.x4, main.y4, width=10.0, fill="red")
                canvas.pack(fill=BOTH, expand=1)

root = Tk()
ex = Render()
root.attributes('-fullscreen', True)
root.mainloop()