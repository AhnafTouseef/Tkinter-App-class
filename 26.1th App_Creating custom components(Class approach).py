import tkinter as tk
from tkinter import ttk

# setup 
wd = tk.Tk()
wd.geometry('400x600')
wd.title('Widget and return')

class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text):
        super().__init__(master= parent)

        # grid layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1,2), weight=1, uniform='a')

        # widget
        ttk.Label(self, text=label_text).grid(row=0, column=0, sticky='nsew')
        ttk.Button(self, text=button_text).grid(row=0, column=1, sticky='nsew')
        self.create_exercise_box('Exercise').grid(row=0, column=2, sticky='nsew')

        self.pack(expand=True, fill='both', padx=10, pady=10)
    
    def create_exercise_box(self, text):
        frame = ttk.Frame(master=self)
        ttk.Entry(frame).pack(expand=True, fill='both')
        ttk.Button(frame, text=text).pack(expand=True, fill='both')

        return frame
        

# Widget
Segment(wd, 'Label', 'Button')
Segment(wd, 'test', 'click')
Segment(wd, 'hello', 'test')
Segment(wd, 'Label', 'Button')
Segment(wd, 'test', 'click')


# run 
wd.mainloop()