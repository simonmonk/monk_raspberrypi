#07_10_menus.py

from tkinter import *

class App:
	
    def __init__(self, master):
        self.entry_text = StringVar()
        Entry(master, textvariable=self.entry_text).pack()
        
        menubar = Menu(root)
        
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='Quit', command=exit)
        menubar.add_cascade(label='File', menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label='Fill', command=self.fill)
        menubar.add_cascade(label='Edit', menu=editmenu)
        
        master.config(menu=menubar)

    def fill(self):
        self.entry_text.set('abc') 
        
root = Tk()
app = App(root)

root.mainloop()

