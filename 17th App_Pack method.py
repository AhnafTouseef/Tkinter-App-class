import tkinter as tk
from tkinter import ttk

# setup 
wd = tk.Tk()
wd.geometry('400x600')
wd.title('Pack Method')

# widgets
label1= ttk.Label(wd, text='Label 1', background='red')
label2= ttk.Label(wd, text='Label 2', background='blue')
label3= ttk.Label(wd, text='Label 3', background='green')
Button= ttk.Button(wd, text='A button')


# layout 
label1.pack(side= 'top', expand=True, fill= 'both', padx=10, pady=10)
label2.pack(side= 'left',expand=True, fill='both')
label3.pack(side= 'top', expand=True, fill='both')
Button.pack(side= 'top', expand=True, fill='both')

# run 
wd.mainloop()