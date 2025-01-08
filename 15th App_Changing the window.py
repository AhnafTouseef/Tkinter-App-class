import tkinter as tk
from tkinter import ttk

# setup 
wd = tk.Tk()
wd.geometry('600x400+500+200')
wd.title('More on the window')
wd.iconbitmap('jupyter_app_icon_161280.ico')

# Window Sizes 
wd.minsize(200,100)
# wd.maxsize(800,700)
wd.resizable(True, True)

# Screen Attributes 
print(wd.winfo_screenwidth())
print(wd.winfo_screenheight())

# Window Attributes
wd.attributes('-alpha', 0.95)
wd.attributes('-topmost', True) #Always on top feature

# Security event 
wd.bind('<Escape>', lambda event: wd.quit())

#Disable windows activity
# wd.attributes('-disable', True)

# wd.attributes('-fullscreen', True)

# Get rid of title bar
wd.overrideredirect(True)
grip = ttk.Sizegrip(wd)
grip.pack()
# grip.place(relx=1.0, rely=1.0, anchor='se')

# run 
wd.mainloop()