import tkinter as tk
from tkinter import ttk

# setup 
wd = tk.Tk()
wd.geometry('600x400')
wd.title('Sliders')


# Slider
scale_float= tk.DoubleVar(value=15)
scale = ttk.Scale(wd, 
                  from_=0, 
                  to=25 ,
                  command= lambda value: print(scale_float.get()), 
                  length=300, 
                  orient='vertical',
                  variable=scale_float)
scale.pack()

# Progress bar 
progress = ttk.Progressbar(wd,
                           variable=scale_float,
                           maximum=25,
                           orient='horizontal',
                           mode = 'indeterminate',
                           length= 400)
progress.pack()

progress.start()








# run 
wd.mainloop()