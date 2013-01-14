#07_06_resizing.py

from tkinter import *

class App:
	
    def __init__(self, master):
        frame = Frame(master)
        frame.pack(fill=BOTH, expand=1)
        #Listbox
        listbox = Listbox(frame)
        for item in ['red', 'green', 'blue', 'yellow', 'pink']:
            listbox.insert(END, item)
        listbox.grid(row=0, column=0, sticky=W+E+N+S)

        #Message
        text = Text(frame, relief=SUNKEN)
        text.grid(row=0, column=1, sticky=W+E+N+S)
        text.insert(END, 'word ' * 100)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(0, weight=1)
root = Tk()
app = App(root)
root.geometry("400x300+0+0")
root.mainloop()
