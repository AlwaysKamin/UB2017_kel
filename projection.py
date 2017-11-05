from tkinter import Tk, Canvas, Frame, BOTH


class projection(Frame):
    def __init__(self):
        super().__init__()\

        self.init_ui()
        canvas = Canvas()

    def init_ui(self):
        self.master.title("Lines")


    def draw(self, x, y):
        self.canvas.create_line(x[1], y[1], x[2], y[2], width=10.0, fill="red")
        self.canvas.create_line(x[3], y[3], x[4], y[4], width=10.0, fill="red")
        return

    def display(self):
        self.canvas.pack(fill=BOTH, expand = 1)
        return

root = Tk()
ex = projection()
root.attributes('-fullscreen', True)
root.mainloop()