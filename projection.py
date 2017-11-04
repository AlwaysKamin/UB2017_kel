import Tkinter as tk

class FullScreenApp(object):
    def __init__(self):
        self.tk = Tk()
        return self.tk

root=tk.Tk()
root.attributes('-fullscreen', True)
root.mainloop()