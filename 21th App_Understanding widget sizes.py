import tkinter as tk
from tkinter import ttk

# setup 
wd = tk.Tk()
wd.geometry('400x600')
wd.title('Widget sizes')

label1= ttk.Label(wd, text='Label 1', background='green')
label2= ttk.Label(wd, text='Label 2', background='red', width = 50)


label1.pack()
label2.pack(fill='x')


wdd=ttk.Frame(wd)
wdd.pack(expand=True, fill='both')
label3= ttk.Label(wdd, text='Label 3', background='green')
label4= ttk.Label(wdd, text='Label 4', background='red', width = 50)

wdd.columnconfigure((0,1), weight=1, uniform='a')
wdd.rowconfigure((0,1), weight=1, uniform='a')

label3.grid(row=1, column=1, sticky='nsew')

# run 
wd.mainloop()