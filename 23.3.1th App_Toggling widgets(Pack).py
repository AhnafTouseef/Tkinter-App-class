import tkinter as tk
from tkinter import ttk


# setup 
wd = tk.Tk()
wd.geometry('600x400')
wd.title('Hide Widget')

def toggle_label():
    global label_visible

    if label_visible:
        label.pack_forget()
        label_visible = False
        frame.pack(expand=True, before=Button)
    else:
        frame.pack_forget()
        label.pack(expand=True, before=Button)
        label_visible = True


label_visible = True
label = ttk.Label(wd, text='A Label', background='green')
label.pack(expand=True)

Button = ttk.Button(wd, text='Toggle Label', command=toggle_label)
Button.pack(side='bottom')

frame = ttk.Frame(wd)

# run 
wd.mainloop()


