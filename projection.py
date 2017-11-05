from tkinter import Tk, Canvas, Frame, BOTH


class Render(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        canvas.create_line(15, 75, 400, 75)

        canvas.pack(fill=BOTH, expand=1)


root = Tk()
ex = Render()
root.attributes('-fullscreen', True)
root.mainloop()