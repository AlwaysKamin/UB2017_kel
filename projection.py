from tkinter import Tk, Canvas, Frame, BOTH


class Render(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_line(15, 25, 200, 25)
        canvas.create_line(15, 50, 200, 50)

        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = Render()
    root.attributes('-fullscreen', True)
    root.mainloop()


if __name__ == '__main__':
    main()