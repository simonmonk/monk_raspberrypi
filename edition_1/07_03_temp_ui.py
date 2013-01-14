#07_03_temp_ui.py

from tkinter import *

class App:
	
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        Label(frame, text='deg C').grid(row=0, column=0)
        self.c_var = DoubleVar()
        Entry(frame, textvariable=self.c_var).grid(row=0, column=1)
        Label(frame, text='deg F').grid(row=1, column=0)
        self.result_var = DoubleVar()
        Label(frame, textvariable=self.result_var).grid(row=1, column=1)
        button = Button(frame, text='Convert', command=self.convert)
        button.grid(row=2, columnspan=2)

    def convert(self):
        print('Not implemented')

root = Tk()
root.wm_title('Temp Converter')
app = App(root)
root.mainloop()
