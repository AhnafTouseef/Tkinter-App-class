import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self, title, size):

        # main stup
        super().__init__()
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])
        self.title(title)

        # widget
        self.menu = Menu(self)
        self.main = Main(self)

        # run
        self.mainloop()

class Menu (ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0,y=0,relheight=1,relwidth=0.3)
        self.create_widget()

    def create_widget(self):
        menu_button1 = ctk.CTkButton(self, text='Button 1')
        menu_button2 = ctk.CTkButton(self, text='Button 2')
        menu_button3 = ctk.CTkButton(self, text='Button 3')

        menu_slider1 = ctk.CTkSlider(self, orientation='vertical', width=20)
        menu_slider2 = ctk.CTkSlider(self, orientation='vertical', width=20)

        toggle_frame = ctk.CTkFrame(self)
        menu_toggle1 = ctk.CTkCheckBox(toggle_frame, text='Toggle 1')
        menu_toggle2 = ctk.CTkCheckBox(toggle_frame, text='Toggle 2')

        entry = ctk.CTkEntry(self)

        self.columnconfigure((0,1,2), weight=1, uniform='a')
        self.rowconfigure((0,1,2,3,4), weight=1, uniform='a')
        
        menu_button1.grid(row=0, column=0, sticky='nsew', columnspan=2, pady=4, padx=4)
        menu_button2.grid(row=0, column=2, sticky='nsew', pady=4, padx=4)
        menu_button3.grid(row=1, column=0, sticky='nsew', columnspan=3, pady=4, padx=4)

        menu_slider1.grid(row=2, column=0, sticky='ns', rowspan=2,pady=20)
        menu_slider2.grid(row=2, column=2, sticky='ns', rowspan=2,pady=20)

        toggle_frame.grid(row=4, column=0, sticky='nsew', columnspan=3)
        menu_toggle1.pack(side='left', expand=True)
        menu_toggle2.pack(side='left', expand=True)

        entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor='center')

        # place widget

class Main(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0.3,rely=0, relwidth=0.7, relheight=1)
        Entry(self,'Entry 1','Button 4','green')
        Entry(self,'Entry 2','Button 5','blue')

# Exercise
class Entry(ctk.CTkFrame):
    def __init__(self, parent,label_text, button_text, label_background):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text=label_text, bg_color=label_background)
        button = ctk.CTkButton(self, text=button_text)

        label.pack(expand=True, fill='both')
        button.pack(expand=True, fill='both', pady=10)

        self.pack(side='left', fill='both', expand=True, padx=20, pady=20)



App('Using classes with CustomTkinter', (600,600))