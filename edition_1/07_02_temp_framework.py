#07_02_temp_framework.py

from tkinter import *

class App:
	
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        Label(frame, text='deg C').grid(row=0, column=0)
        button = Button(frame, text='Convert', command=self.convert)
        button.grid(row=1)

    def convert(self):
        print('Not implemented')

root = Tk()
root.wm_title('Temp Converter')
app = App(root)
root.mainloop()
