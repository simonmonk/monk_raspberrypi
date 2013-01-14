#07_05_kitchen_sink.py

from tkinter import *

class App:
	
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        Label(frame, text='Label').grid(row=0, column=0)
        Entry(frame, text='Entry').grid(row=0, column=1)
        Button(frame, text='Button').grid(row=0, column=2)
        check_var = StringVar()
        check = Checkbutton(frame, text='Checkbutton', variable=check_var, onvalue='Y', offvalue='N')
        check.grid(row=1, column=0)
        #Listbox
        listbox = Listbox(frame, height=3, selectmode=SINGLE)
        for item in ['red', 'green', 'blue', 'yellow', 'pink']:
            listbox.insert(END, item)
        listbox.grid(row=1, column=1)
        #Radiobutton set
        radio_frame = Frame(frame)
        radio_selection = StringVar()
        b1 = Radiobutton(radio_frame, text='portrait', 
            variable=radio_selection, value='P')
        b1.pack(side=LEFT)
        b2 = Radiobutton(radio_frame, text='landscape', 
            variable=radio_selection, value='L')
        b2.pack(side=LEFT)
        radio_frame.grid(row=1, column=2)
        #Scale
        scale_var = IntVar()
        Scale(frame, from_=1, to=10, orient=HORIZONTAL,
              variable=scale_var).grid(row=2, column=0)
        Label(frame, textvariable=scale_var, 
              font=("Helvetica", 36)).grid(row=2, column=1)
        #Message
        message = Message(frame, 
              text='Multiline Message Area')
        message.grid(row=2, column=2)
        #Spinbox
        Spinbox(frame, values=('a','b','c')).grid(row=3)
root = Tk()
root.wm_title('Kitchen Sink')
app = App(root)
root.mainloop()
