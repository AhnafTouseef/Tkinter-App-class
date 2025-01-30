import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Extra(tk.Toplevel):
    def __init__(self):
        super().__init__()   
        x, y = 300,400
        self.geometry(f'{x}x{y}')
        self.title('Extra Windows')
        ttk.Label(self, text='A label').pack()
        ttk.Button(self, text='A Button', command=create_window).pack()
        ttk.Label(self, text='Another label').pack(expand = True)


def ask_yes_no():
    answer = messagebox.askquestion('Title', 'Are you in?')

    if answer == 'yes':
        messagebox.showinfo('Title','Right answer')
    else:
        messagebox.showerror('Title','Wrong answer')

def create_window():
    global extra_window
    extra_window = Extra()
def close_window():
    extra_window.destroy()

# setup 
wd = tk.Tk()
x, y = 400,400
wd.geometry(f'{x}x{y}')
wd.title(' Multiple Windows')

button1 = ttk.Button(wd, text='Open main window', command=create_window)
button1.pack(expand=True)

button2 = ttk.Button(wd, text='Close main window', command=close_window)
button2.pack(expand=True)

button3 = ttk.Button(wd, text='Craete yes no  window', command=ask_yes_no)
button3.pack(expand=True)





# run 
wd.mainloop()