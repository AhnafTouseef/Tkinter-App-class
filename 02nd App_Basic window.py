import tkinter as tk
from tkinter import ttk

def custom_funtion():
    window = tk.Tk()
    window.title('Funtionally called window')
    window.geometry('350x50')

    label = ttk.Label(master=window, text= 'Hashmap MadaFAqa')
    label.pack()

    window.mainloop()

# create window
wd = tk.Tk()
wd.title('Ivysaur')
wd.geometry('800x600')

# create widgets
tk.Text(master=wd).pack()

# ttk widgets
label = ttk.Label(master=wd, text= 'This is a text')
label.pack()

# ttk entry
entry = ttk.Entry(master=wd)

# ttk botton
button = ttk.Button(master=wd, text='Hit it!!', command = custom_funtion)

# Exercise label
label_exercise = ttk.Label(master=wd, text= 'Nigga Label')

# Exercise button
Button_exercise= ttk.Button(master=wd, text='Hail Hittler', command= lambda: print('Hail Hittler'))

# packing
entry.pack()
label_exercise.pack()
button.pack()
Button_exercise.pack()

# run
wd.mainloop()
