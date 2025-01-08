import tkinter as tk
from tkinter import ttk


# setup 
wd = tk.Tk()
wd.geometry('600x400')
wd.title('Hide Widget')

# place 
def toggle_label():
    global label_visible
    
    if label_visible:
        label.place_forget()
        label_visible=False
    else:
        label.place(relx=0.5, rely=0.5, anchor='center')
        label_visible=True

Button = ttk.Button(wd, text='Toggle Label', command=toggle_label)
Button.place(x=10, y=10)

label_visible=True
label = ttk.Label(wd, text='A Label', background='green')
label.place(relx=0.5, rely=0.5, anchor='center')


# run 
wd.mainloop()


