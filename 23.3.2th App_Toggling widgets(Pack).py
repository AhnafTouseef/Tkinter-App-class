import tkinter as tk
from tkinter import ttk


# setup 
wd = tk.Tk()
wd.geometry('600x400')
wd.title('Hide Widget')

def toggle_label():
    label.pack_forget() if label.winfo_ismapped() else label.pack(expand=True)
    

label = ttk.Label(wd, text='A Label', background='green')
label.pack(expand=True)

Button = ttk.Button(wd, text='Toggle Label', command=toggle_label)
Button.pack(side='bottom')

# run 
wd.mainloop()


