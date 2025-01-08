import tkinter as tk
from tkinter import ttk


# setup 
wd = tk.Tk()
wd.geometry('600x400')
wd.title('Hide Widget')

# place 
def toggle_label():
    label.place_forget() if label.winfo_ismapped() else label.place(relx=0.5, rely=0.5, anchor='center')
    
Button = ttk.Button(wd, text='Toggle Label', command=toggle_label)
Button.place(x=10, y=10)

label = ttk.Label(wd, text='A Label', background='green')
label.place(relx=0.5, rely=0.5, anchor='center')


# run 
wd.mainloop()


