
import tkinter as tk
from tkinter import ttk

def button_func():
    print(str_var.get())

# Window 
wd = tk.Tk()
wd.title('Tkinter variables')

# tkiter variable 
str_var = tk.StringVar(value='start value')


# widget 
label = ttk.Label(master=wd, text='Label', textvariable= str_var)
label.pack()

entry = ttk.Entry(master=wd, textvariable= str_var)
entry.pack()

Button = ttk.Button(master=wd, textvariable= str_var, command= button_func)
Button.pack()

# Exercise 
str_ex_var = tk.StringVar(value='Exercise')

labe_ex1 = ttk.Label(master=wd, textvariable=str_ex_var )
labe_ex1.pack()
labe_ex2 = ttk.Label(master=wd, textvariable=str_ex_var )
labe_ex2.pack()

entry_ex = ttk.Entry(master=wd, textvariable=str_ex_var)
entry_ex.pack()
# Run 
wd.mainloop()


