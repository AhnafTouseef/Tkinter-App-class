import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

# Window
wd = ctk.CTk()
wd.title('Custom Tkinter App')
x, y = 4,4
wd.geometry(f'{x}00x{y}00')

# Widget
string_var = tk.StringVar(value = 'a custom string')
label = ctk.CTkLabel(wd,
                     text='A ctk label',
                     fg_color=('red','blue'),
                     text_color=('Black','white'),
                     corner_radius=10,
                     textvariable=string_var)
label.pack()

button = ctk.CTkButton(wd,
                       text='A ctk button',
                       fg_color=('red','blue'),
                       text_color=('Black','white'),
                       corner_radius=10,
                       hover_color=('green','yellow'),
                       command=lambda: ctk.set_appearance_mode('light'))
button.pack()

frame = ctk.CTkFrame(wd)
frame.pack()

slider = ctk.CTkSlider(frame)
slider.pack(padx=20,pady=20)

# Exercise
switch = ctk.CTkSwitch(wd,
                       text='Exercise switch',
                       fg_color='red',
                       progress_color='blue',
                       button_color='green',
                       button_hover_color='lime',
                       switch_width=60,
                       switch_height=30,
                       corner_radius=10
                       )
switch.pack()



wd.mainloop()