import sys
import ctypes
from tkinter import *
#from sdl2 import*
class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame,
                         text="Scan Block",
                         command=quit)
    self.button.grid(row=0, column=0)
    self.button2 = Button(frame,
                         text="Display on Block",
                         command=quit)
    self.button2.grid(row=0, column=1)

def main():
    root = Tk()
    root.title("Apprentice")
    root.geometry("900x800")
    app = App(root)
    root.mainloop()

