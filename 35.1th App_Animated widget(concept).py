import customtkinter as ctk
from random import choice

# Funtions to move and configure the buttons and do some stuffs
def move_btn():
    global button_x
    button_x +=0.05
    if button_x < 1:
        button.place(relx =button_x, rely=0.5, relheight=button_x, anchor='center')
        colors = ['red', 'yellow', 'pink', 'green', 'blue', 'black', 'white']
        color = choice(colors)
        button.configure(fg_color= color)
        wd.after(100, move_btn) # Delay funtion calling

def infinite_print():
    global button_xx
    button_xx +=0.001
    if button_xx < 0.9:
        print('infinite')
        button1.place(relx =button_xx, rely=0.5, anchor='nw')
        print(button_xx)
        wd.after(10, infinite_print) # Delay funtion calling


# Window
wd = ctk.CTk()
wd.title('Animated widget')
wd.geometry('600x400')

#button
button_x =0.5
button_xx =0.5

# Button with moving funtionality
button = ctk.CTkButton(wd, text='toggle sidebar', command=move_btn)
button.place(relx= button_x, rely= 0.5, relheight=button_x, anchor= 'center')

#Exercise
# Button with infinite print funtionality
button1 = ctk.CTkButton(wd, text='toggle sidebar1', command=infinite_print)
button1.place(relx= button_x, rely= 0.5, anchor= 'nw')

#run
wd.mainloop()
