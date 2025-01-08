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

# Pack 
label1.pack(side='left', expand=True, fill='x')
label2.pack(side='left', expand=True, fill='both')
label3.pack(side='top', expand=False, fill='both')

# run 
wd.mainloop()



