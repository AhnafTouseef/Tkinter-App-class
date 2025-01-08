import tkinter as tk
from tkinter import ttk

# setup 
wd = tk.Tk()
wd.geometry('400x600')
wd.title('Place')

# widgets
label1= ttk.Label(wd, text='Label 1', background='red')
label2= ttk.Label(wd, text='Label 2', background='blue')
label3= ttk.Label(wd, text='Label 3', background='green')
Button= ttk.Button(wd, text='Button ')

# layout 
label1.place(x=300,y=100, width=100, height=200)
label2.place(relx=0.2,rely=0.1, relwidth=0.4, relheight=0.5)
label3.place(x=80,y=60, width=160, height=300)
Button.place(relx=1, rely=1, anchor='se')

# frame
frame = ttk.Frame(wd)
frame_label = ttk.Label(frame, text='Frame Label', background='yellow')
frame_button = ttk.Button(frame, text='Frame Button')

# frame layout 
frame.place(relx = 0, rely = 0, relwidth=0.3, relheight=1)
frame_label.place(relx=0,rely=0,relwidth=1,relheight=1/2)
frame_button.place(relx=0,rely=0.5,relwidth=1,relheight=1/2)

# exercise
exrcise_label = ttk.Label(wd, text=' Exercise label', background='orange')
exrcise_label.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.5, height=200)

ttk.Sizegrip().place(relx=1,rely=1,anchor='se')
# run 
wd.mainloop()