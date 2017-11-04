import tkinter as tk

class FullScreenApp(object):
    def __init__(self):
        self.tk = tk()
        return self.tk

root=tk.Tk()
root.attributes('-fullscreen', True)
root.mainloop()