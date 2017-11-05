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


    def draw(self, template, m, n):
        print("Drawing")
        self.init_ui()
        print("Printing line at: " + str(template.x[0]) + " " + str(template.y[0]) + " " + str(template.x[1]) + " " + str(template.y[1]))
        print("Printing line at: " + str(template.x[2]) + " " + str(template.y[2]) + " " + str(template.x[3]) + " " + str(template.y[3]))
        self.canvas.create_line(template.x[0], template.y[0], template.x[1], template.y[2], width=10.0, fill="red")
        self.canvas.create_line(template.x[2], template.y[2], template.x[3], template.y[3], width=10.0, fill="red")
        self.canvas.pack(fill=BOTH, expand = 1)
        return

    def display(self):
        print("Displaying")
        self.canvas.pack(fill=BOTH, expand = 1)
        return
