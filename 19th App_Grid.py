import tkinter as tk
from tkinter import ttk

# setup 
wd = tk.Tk()
wd.geometry('600x400')
wd.title('Grid')

# widgets
label1= ttk.Label(wd, text='Label 1', background='red')
label2= ttk.Label(wd, text='Label 2', background='blue')
label3= ttk.Label(wd, text='Label 3', background='green')
label4= ttk.Label(wd, text='Label 3', background='yellow')
Button1= ttk.Button(wd, text='Button 1')
Button2= ttk.Button(wd, text='Button 2')
entry = ttk.Entry(wd)

# define grid
wd.columnconfigure((0,1,2), weight=1, uniform='a')
wd.columnconfigure(3, weight=3, uniform='a')
wd.rowconfigure((0,1,2), weight=1, uniform='a')
wd.rowconfigure(3, weight=3, uniform='a')

# place widget
label1.grid(row=0,column=0, sticky='nsew')
label2.grid(row=1,column=1,rowspan=3, sticky='nsew')
label3.grid(row=1,column=0,columnspan=3, sticky='nsew',padx=20,pady=10)
label4.grid(row=3,column=3,columnspan=3, sticky='se')

# Exercise 
Button1.grid(row=0,column=3, sticky='nesw')
Button2.grid(row=2,column=2, sticky='nesw')
entry.grid(row=2, column=3, rowspan=2, sticky='ew')


# run 
wd.mainloop()