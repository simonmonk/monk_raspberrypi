#07_09_color_chooser.py

from tkinter import *
import tkinter.colorchooser as cc

class App:
	
    def __init__(self, master):
        b=Button(master, text='Color..', command=self.ask_color).pack()

    def ask_color(self):
        (rgb, hx) = cc.askcolor()
        print("rgb=" + str(rgb) + " hx=" + hx)

root = Tk()
app = App(root)
root.mainloop()
