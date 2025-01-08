import tkinter as tk
from tkinter import ttk

# setup 
wd = tk.Tk()
wd.geometry('600x400')
wd.title('Layout')

# Widget 
label1 = ttk.Label(wd, text='label 1', background='red')
label2 = ttk.Label(wd, text='label 2', background='blue')
label3 = ttk.Label(wd, text='label 3', background='yellow')

# Grid 
wd.columnconfigure(0, weight=1)
wd.columnconfigure(1, weight=1)
wd.columnconfigure(2, weight=2)
wd.rowconfigure(0, weight=1)
wd.rowconfigure(1, weight=1)

label1.grid(row=0, column=1, sticky='nsew')
label2.grid(row=0, column=0, sticky='nsew')
label3.grid(row=1, column=1, columnspan=2, sticky='nsew')


# run 
wd.mainloop()



