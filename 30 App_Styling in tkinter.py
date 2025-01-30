import tkinter as tk
from tkinter import ttk, font
import random

# setup 
wd = tk.Tk()
x, y = 4,5
wd.geometry(f'{x}00x{y}00')
wd.title('Styling')

# Random fonts
Font = random.choice(font.families())
Font2 = random.choice(font.families())
Font3 = random.choice(font.families())

# Custom Styling
style = ttk.Style()
Style_name=random.choice(style.theme_names())
style.theme_use(Style_name)

style.configure('TButton', foreground = 'green', font =('Jokerman', 20))

style.configure('new.TButton', foreground = 'red', font =(Font2, 20))
style.map('new.TButton', foreground=[('pressed', 'blue')])

style.configure('new2.TButton', foreground = 'red', font =(Font3, 20))
style.map('new2.TButton', foreground=[('pressed', 'blue'), ('disabled', 'purple')])


# widget 
label = ttk.Label(wd, 
                  text=Font, 
                  background= 'red', 
                  foreground='white',
                  font=(Font, 20),
                  justify='center'
                  )
label.pack()


button1 = ttk.Button(wd, text=Style_name, cursor='hand2')
button1.pack()
button2 = ttk.Button(wd, text=Style_name, cursor='hand2', style='new.TButton')
button2.pack()
button3 = ttk.Button(wd, text=Style_name, cursor='hand2', style='new2.TButton', state='disabled')
button3.pack()


ttk.Label(wd, 
            text=f'{style.theme_names()}'.replace('(','').replace(')','').replace("'",""), 
            background= 'grey', 
            justify='center'
            ).pack(expand=True)

# Exercise
style.configure('TFrame', background ='pink')
frame = ttk.Frame(wd, height=200, width=100)
frame.pack()

# run 
wd.mainloop()