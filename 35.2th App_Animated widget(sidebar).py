import customtkinter as ctk
from random import choice


class sidepanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master = parent, fg_color='grey')

        self.startpos = start_pos + 0.02
        self.endpos = end_pos - 0.02
        self.width = abs(end_pos - start_pos)

        # Animation logic
        self.pos = self.startpos
        self.in_start_pos = True

        self.place(relx=self.startpos, rely=0.05, relwidth=self.width, relheight=0.9)

    def animate(self):
        if self.in_start_pos:
            self.animate_leftward()
        else:
            self.animate_rightward()

    def animate_leftward(self):
        if self.pos > self.endpos:
            self.pos -= 0.01
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_leftward)
        else:
            self.in_start_pos = False

    def animate_rightward(self):
        if self.pos < self.startpos:
            self.pos += 0.01
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_rightward)
        else:
            self.in_start_pos = True

# Funtions to move and configure the buttons and do some stuffs

# Window
wd = ctk.CTk()
wd.title('Animated widget')
wd.geometry('600x400')

def toggle_nightmode():
    if ctk.get_appearance_mode() == 'Dark':
        ctk.set_appearance_mode('Light')
    else:
        ctk.set_appearance_mode('Dark')

# Animated sidebar
animated_panel1 = sidepanel(wd, 1, 0.7)
ctk.CTkLabel(animated_panel1, text='Sidebar right').pack(expand=True, fill='both', padx = 10, pady = 10)
ctk.CTkLabel(animated_panel1, text='Label 2').pack(expand=True, fill='both', padx = 10, pady = 10)
ctk.CTkButton(animated_panel1, text='Label 2', corner_radius= 10, command=toggle_nightmode).pack(expand=True, fill='both', padx = 10, pady = 10)
ctk.CTkTextbox(animated_panel1, corner_radius= 10, fg_color= ('#dbdbdb', '#2b2b2b')).pack(expand=True, fill='both', padx = 10, pady = 10)

animated_panel2 = sidepanel(wd, 0.0, -0.3)
ctk.CTkLabel(animated_panel2, text='Sidebar left ').pack(expand=True, fill='both', padx = 10, pady = 10)
ctk.CTkLabel(animated_panel2, text='Label 2').pack(expand=True, fill='both', padx = 10, pady = 10)
ctk.CTkButton(animated_panel2, text='Label 2', corner_radius= 10, command=toggle_nightmode).pack(expand=True, fill='both', padx = 10, pady = 10)
ctk.CTkTextbox(animated_panel2, corner_radius= 10, fg_color= ('#dbdbdb', '#2b2b2b')).pack(expand=True, fill='both', padx = 10, pady = 10)

#button
button1 = ctk.CTkButton(wd, text='Toggle sidebar right', command=animated_panel1.animate)
button1.place(relx= 0.5, rely= 0.3, anchor= 'center')
button2 = ctk.CTkButton(wd, text='Toggle sidebar left', command=animated_panel2.animate)
button2.place(relx= 0.5, rely= 0.4, anchor= 'center')


#run
wd.mainloop()
