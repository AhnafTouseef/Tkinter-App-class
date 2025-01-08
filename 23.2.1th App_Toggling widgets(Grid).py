import tkinter as tk
from tkinter import ttk


# setup 
wd = tk.Tk()
wd.geometry('600x400')
wd.title('Hide Widget')

def toggle_label():
    global label_visible

    if label_visible:
        label.grid_remove()
        label_visible = False
    else:
        label.grid(row=0, column=1)
        label_visible = True

wd.columnconfigure((0,1), weight=1, uniform='a')
wd.rowconfigure(0, weight=1, uniform='a')
    
Button = ttk.Button(wd, text='Toggle Label', command=toggle_label)
Button.grid(row=0, column=0)

label_visible = True
label = ttk.Label(wd, text='A Label', background='green')
label.grid(row=0, column=1)


# run 
wd.mainloop()


