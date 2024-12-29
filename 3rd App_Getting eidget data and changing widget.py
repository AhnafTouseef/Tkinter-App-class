import tkinter as tk
from tkinter import ttk

def button_func():
    # get content of the entry 
    entry_text = entry.get()

    # upgrade the label 
    # label.config(text='some other text')
    label['text'] = entry_text

    # dissable input field after button press 
    entry['state']= 'disabled'

# Window
window = tk.Tk()
window.title('Getting and setting widgets')
window.geometry('500x100')

# Widgets 
label = ttk.Label(master=window, text='This is the label')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text='This one is the button', command = button_func)
button.pack()

def reset_funtion():
    label['text'] = 'This is the label'
    entry['state']= 'enabled'
    pass

button = ttk.Button(master=window, text='Exercise button', command = reset_funtion)
button.pack()



# Run 
window.mainloop()