import tkinter as tk
from tkinter import ttk

# setup 
wd = tk.Tk()
wd.geometry('400x600')
wd.title('Pack Parenting')

# widgets
# Top frame
top_frame = ttk.Frame(wd)
label1= ttk.Label(top_frame, text ='Label 1', background ='red')
label2= ttk.Label(top_frame, text ='Label 2', background ='blue')
# middle widget 
label3= ttk.Label(wd, text ='Label 3', background ='green')

# bottom frame 
bottom_frame = ttk.Frame(wd)
label4= ttk.Label(bottom_frame, text ='Label 3', background ='orange')
Button= ttk.Button(bottom_frame, text ='A button')
Button1= ttk.Button(bottom_frame, text ='Another button')

# Top layout 
label1.pack(side='left',fill='both', expand=True)
label2.pack(side='left',fill='both', expand=True)
top_frame.pack(fill='both', expand=True)

# middle layout 
label3.pack(expand=True)

# bottom layout 
Button.pack(side='left', expand= True, fill='both')
label4.pack(side='left', expand= True, fill='both')
Button1.pack(side='left', expand= True, fill='both')
bottom_frame.pack(expand=True, fill='both', padx=20, pady=20)

# Exercise 
exercise_frame = ttk.Frame(bottom_frame)
Button2= ttk.Button(exercise_frame, text ='A button2')
Button3= ttk.Button(exercise_frame, text ='A button3')
Button4= ttk.Button(exercise_frame, text ='A button4')

Button2.pack(expand= True, fill='both')
Button3.pack(expand= True, fill='both')
Button4.pack(expand= True, fill='both')
exercise_frame.pack(side='left',expand= 0, fill='both')


wd.bind('<Escape>', lambda event: wd.quit())
# run 
wd.mainloop() 