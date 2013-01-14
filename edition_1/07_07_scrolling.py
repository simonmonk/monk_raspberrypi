#07_07_scrolling.py

from tkinter import *

class App:
	
    def __init__(self, master):
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)
        text = Text(master, yscrollcommand=scrollbar.set)
        text.pack(side=LEFT, fill=BOTH)
        text.insert(END, 'word ' * 1000)
        scrollbar.config(command=text.yview)

root = Tk()
root.wm_title('Scrolling')
app = App(root)
root.mainloop()
