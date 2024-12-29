import tkinter as tk
import ttkbootstrap as ttk

def convert():
    mile = entry_int.get()
    km = mile*1.61
    output_string.set(km)



# window
wd = ttk.Window(themename='darkly')
wd.title('Bulbasaur')
wd.geometry('300x150')


#title
title_label = ttk.Label(master =wd, text = 'Miles to Kilometers', font = 'Calibri 24 bold')
title_label.pack()


# input field
input_frame = ttk.Frame(master = wd)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable= entry_int)
button = ttk.Button(master = input_frame, text = 'Covert', command= convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady = 10)

# output field
output_string = tk.StringVar()
output_label= ttk.Label(master=wd, text = 'Output', font='Calibri 24', textvariable=output_string)
output_label.pack()

# run
wd.mainloop()