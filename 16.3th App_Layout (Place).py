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

label1.place(x = 100, y=200, width = 200, height = 100)
label2.place(relx = 0.3, rely=0.4, relwidth = 1.5, height = 100, anchor='se')
label3.place(x=10,y=10, relwidth=0.2)

# run 
wd.mainloop()



