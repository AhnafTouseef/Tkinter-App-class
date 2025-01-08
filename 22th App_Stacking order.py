import tkinter as tk
from tkinter import ttk

# setup 
wd = tk.Tk()
wd.geometry('400x400')
wd.title('Stacking order')

# widget 
label1= ttk.Label(wd, text='Label 1', background='green')
label2= ttk.Label(wd, text='Label 2', background='red')
label3= ttk.Label(wd, text='Label 3', background='orange')

button1 = ttk.Button(wd, text='raise label 1', command= lambda:label1.tkraise(aboveThis = label2))
button2 = ttk.Button(wd, text='raise label 2', command= lambda:label2.tkraise())
button3 = ttk.Button(wd, text='raise label 3', command= lambda:label3.tkraise())

# layout 
label1.place(x=50,y=100,width=200, height=150)
label2.place(x=150,y=60,width=140, height=100)
label3.place(x=100,y=50,width=140, height=100)

button1.place(relx=0.6, rely=1,anchor='se')
button2.place(relx=0.8, rely=1,anchor='se')
button3.place(relx=1, rely=1,anchor='se')

# run 
wd.mainloop()