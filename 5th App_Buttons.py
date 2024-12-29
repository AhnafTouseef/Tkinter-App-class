import tkinter as tk
from tkinter import ttk

# setup 
wd = tk.Tk()
wd.title('Buttons')
wd.geometry('600x400')

# butoons 
def button_func():
    print('a basic button')
    print(radio_var.get())
button = ttk.Button(wd, text="Simple button 1", command=button_func)
button.pack()

button_string = tk.StringVar(value='Button eith string var')
button = ttk.Button(wd, text="Simple button 2", 
                    command=lambda: print('A 2nd basic button'),
                    textvariable=button_string
                    )
button.pack()

# checkbox 
check_var = tk.IntVar()
check1 = ttk.Checkbutton(wd, text='checkbox 1',
                        command=lambda: check_var.set(5),
                        )
check1.pack()

check2 = ttk.Checkbutton(wd, text='checkbox 2',
                         command=lambda: print(check_var.get()),
                         variable= check_var,
                         onvalue= 5,
                         offvalue=10
                         )
check2.pack()

# Radio buttons 
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(wd, text='Radio button 1', value = 'any shit',
                         variable=radio_var, command=lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(wd, text='Radio button 2', value= 2, variable=radio_var,
                         command=lambda: print(radio_var.get()))
radio2.pack()

# Exercise 
ttk.Label(wd, text='''________________________________________________________________________
                                                Excercise
________________________________________________________________________''').pack()
def radio_func():
    print(check_bool.get())
    check_bool.set(False)
    pass


radio_string = tk.StringVar()
check_bool = tk.BooleanVar()

exercise_radio1= ttk.Radiobutton(wd, text= 'Radio A', value= 'A', command=radio_func, variable=radio_string)
exercise_radio2= ttk.Radiobutton(wd, text= 'Radio B', value= 'B', command=radio_func, variable=radio_string)
exercise_check = ttk.Checkbutton(wd, text='Exercise check', variable= check_bool, command=lambda: print(radio_string.get()))
exercise_radio1.pack()
exercise_radio2.pack()
exercise_check.pack() 



# run 
wd.mainloop()