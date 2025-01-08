import tkinter as tk
from tkinter import ttk

# setup 
wd = tk.Tk()
wd.geometry('400x600')
wd.title('Widget and return')

def create_segment(parent, label_text, button_text):
        frame = ttk.Frame(parent)

        # grid layout
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure((0,1,2), weight=1, uniform='a')

        # widget
        ttk.Label(frame, text=label_text).grid(row=0, column=0, sticky='nsew')
        ttk.Button(frame, text=button_text).grid(row=0, column=1, sticky='nsew')
        
        return frame
        

# Widget
create_segment(wd, 'Label', 'Button').pack(fill='both', expand=True, padx=10,pady=10)
create_segment(wd, 'test', 'click').pack(fill='both', expand=True, padx=10,pady=10)
create_segment(wd, 'hello', 'test').pack(fill='both', expand=True, padx=10,pady=10)
create_segment(wd, 'Label', 'Button').pack(fill='both', expand=True, padx=10,pady=10)
create_segment(wd, 'test', 'click').pack(fill='both', expand=True, padx=10,pady=10)


# run 
wd.mainloop()