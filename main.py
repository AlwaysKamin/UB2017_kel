# from tkinter import *
#
# class Example(Frame):
#
#     def __init__(self, parent):
#         Frame.__init__(self, parent, background="green")
#
#         self.parent = parent
#
#         self.parent.title("Window")
#         self.pack(fill=BOTH, expand=1)
#
# # creates window
# root = Tk()
#
# root.title("Apprentice")
# root.geometry("900x800")
#
# # app = Frame(root)
# # app.grid()
# # button1 = Button(app, text="Scan Block")
# # button.grid()
#
# # kicks off main root.
# root.mainloop()



from tkinter import *
class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame,
                         text="Scan Block", fg="red",
                         command=quit)
    self.button.pack(side=LEFT)
    self.button2 = Button(frame,
                         text="Display on Block",
                         command=quit)
    self.button2.pack(side=LEFT)


root = Tk()
root.title("Apprentice")
root.geometry("900x800")
app = App(root)
root.mainloop()

