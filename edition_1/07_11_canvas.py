#07_11_canvas.py

from tkinter import *

class App:
	
    def __init__(self, master):
        canvas = Canvas(master, width=400, height=200)
        canvas.pack()
        canvas.create_rectangle(20, 20, 300, 100, fill='blue')
        canvas.create_oval(30, 50, 290, 190, fill='#ff2277')
        canvas.create_line(0, 0, 400, 200, fill='black', width=5)        
root = Tk()
app = App(root)
root.mainloop()
