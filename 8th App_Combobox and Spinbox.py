import tkinter as tk
from tkinter import ttk

# setup 
wd = tk.Tk()
wd.geometry('600x400')
wd.title('Combo box & spin box')

# Combobox 

item = ('Ice cream', 'Pizza', 'Burger')
# Method 1 
combo = ttk.Combobox(wd)
combo['values'] = item
combo.pack()
# Method 2
combo2 = ttk.Combobox(wd)
combo2.config(values=item)
combo2.pack()
# Setting default value 
food_string = tk.StringVar(value=item[1])
combo3 = ttk.Combobox(wd, textvariable=food_string)
combo3.config(values=item)
combo3.pack()

# events
combo3.bind('<<ComboboxSelected>>', lambda event: print(food_string.get()))

combo_label =  ttk.Label(wd,text='a abel', textvariable = food_string)
combo_label.pack()

# Spinbox 
spin = ttk.Spinbox(wd)
spin['value']=(1,2,3,4,5)
spin.pack()

spin_int = tk.IntVar(value=12)
spin2 = ttk.Spinbox(wd, from_=3, to=20, increment=3, command=lambda : print(spin_int.get()), textvariable=spin_int)
spin2.bind('<<Increment>>', lambda event: print('Up'))
spin2.bind('<<Decrement>>', lambda event: print('Down'))
spin2.pack()


# Exercise
spin_ex_str = tk.StringVar(value='A')
spin_ex = ttk.Spinbox(wd, text ='Exercise string', textvariable=spin_ex_str)
spin_ex['value']=('A','B','C','D','E')
spin_ex.bind('<<Decrement>>', lambda event: print(spin_ex_str.get()))
spin_ex.pack()



# run 
wd.mainloop()