import tkinter as tk
from tkinter import ttk

def button_func(entry_string):
    print('A button was pressed')
    print(entry_string.get())

# setup 
wd = tk.Tk()
wd.title('Buttons, functions and arguments')

# widget
entry_string = tk.StringVar(value='test')
entry = ttk.Entry(wd, textvariable=entry_string)
entry.pack()

ttk.Button(wd, text='button', command= lambda: button_func(entry_string)).pack()


# Run 
wd.mainloop()
