import tkinter as tk
from tkinter import ttk

# setup 
wd = tk.Tk()
wd.geometry('600x400')
wd.title('Tabs')

# Notebook widget 
notebook = ttk.Notebook(wd, height=200, width=200)

tab1 = ttk.Frame(notebook, relief='sunken')
ttk.Label(tab1, text= 'Text in tab 1').pack()
ttk.Button(tab1, text= 'Button in tab 1').pack()

tab2 = ttk.Frame(notebook, relief='groove')
ttk.Label(tab2, text= 'Label in tab 2').pack()
ttk.Button(tab2, text= 'Button in tab 2').pack()


notebook.add(tab1, text= 'Tab 1')
notebook.add(tab2, text= 'Tab 2')

# exercise
tab3 = ttk.Frame(notebook, relief='raised')
ttk.Button(tab3, text= 'Button in tab 3').pack()
ttk.Button(tab3, text= 'Button in tab 3').pack()
ttk.Label(tab3, text='Exercise label').pack()
notebook.add(tab3, text='Tab 3')

notebook.pack()

# run 
wd.mainloop()