from tkinter import Tk, Canvas, Frame, BOTH


class projection(Frame):
    def __init__(self):
        super().__init__()\

        self.init_ui()
        canvas = canvas(self)

    def init_ui(self):
        self.master.title("Lines")

        fileName = open("templates/firstReadInTest.block", "r")

        for line in fileName:
            if ('L' or 'H') in line:
                self.pack(fill=BOTH, expand=1)
                # canvas = Canvas(self)
                canvas.create_line(main.x1, main.y1, main.x2, main.y2, width=10.0, fill="red")
                canvas.create_line(main.x3, main.y3, main.x4, main.y4, width=10.0, fill="red")
                canvas.pack(fill=BOTH, expand=1)

    def draw(self, x, y):
        self.canvas.create_line(x[1], y[1], x[2], y[2], width=10.0, fill="red")
        return

    def display(self):
        self.canvas.pack(fill=BOTH, expand = 1)
        return

root = Tk()
ex = projection()
root.attributes('-fullscreen', True)
root.mainloop()