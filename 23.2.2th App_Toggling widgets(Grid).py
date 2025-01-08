import tkinter as tk
from tkinter import ttk


# setup 
wd = tk.Tk()
wd.geometry('600x400')
wd.title('Hide Widget')

def toggle_label():
    if label.winfo_viewable():
        label.grid_remove()
    else:
        label.grid()

wd.columnconfigure((0,1), weight=1, uniform='a')
wd.rowconfigure(0, weight=1, uniform='a')
    
Button = ttk.Button(wd, text='Toggle Label', command=toggle_label)
Button.grid(row=0, column=0)

label = ttk.Label(wd, text='A Label', background='green')
label.grid(row=0, column=1)


# run 
wd.mainloop()


