from tkinter import *
from template import template2x4


class projection(Frame):
    def __init__(self):
        super().__init__()\

        self.init_ui()
        projection = Toplevel()
        projection.title("Second window")
        projection.attributes('-fullscreen', True)
        self.canvas = Canvas(projection)

    def init_ui(self):
        self.master.title("Lines")


    def draw(self, template):
        print("Drawing")
        self.init_ui()
        self.canvas.create_line(template.x[1], template.y[1], template.x[2], template.y[2], width=10.0, fill="red")
        self.canvas.pack(fill=BOTH, expand = 1)
        return

    def display(self):
        print("Displaying")
        self.canvas.pack(fill=BOTH, expand = 1)
        return
