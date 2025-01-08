import tkinter as tk
from tkinter import ttk

# setup 
wd = tk.Tk()
wd.geometry('600x400')
wd.title('Frames and Parenting')

# Frame
frame = ttk.Frame(wd, width=200, height=200, borderwidth=10, relief= tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side='left')

# master setting 
label = ttk.Label(frame, text='label in frame')
label.pack()

button = ttk.Button(frame, text='Button in frame')
button.pack()

label = ttk.Label(wd, text='label outside frame')
label.pack(side='left')

# exercise 
exercise_frame = ttk.Frame(wd, width=200, height=200, borderwidth=10, relief= tk.GROOVE)
exercise_frame.pack_propagate(False)
exercise_frame.pack(side='left')

exercise_label = ttk.Label(exercise_frame, text='label in frame')
exercise_label.pack()

exercise_button = ttk.Button(exercise_frame, text='Button in frame')
exercise_button.pack()

exercise_entry = ttk.Entry(exercise_frame)
exercise_entry.pack()


# run 
wd.mainloop()