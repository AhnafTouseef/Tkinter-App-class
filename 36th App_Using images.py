import tkinter as tk
from tkinter import ttk 
import customtkinter as ctk
from PIL import Image, ImageTk


# Main window
wd = ctk.CTk()
wd.geometry('700x700')
wd.title('Using images')

# Grid layout
wd.columnconfigure((0,1,2,3), weight=1,uniform='a')
wd.rowconfigure((0,1), weight=1)

# Importing a big image
image_original = Image.open('python wall paper.jpg')
image_ratio = image_original.width / image_original.height
image_tk = ImageTk.PhotoImage(image_original)

# Importing image for icon for ttk.button
dark_image = Image.open('python_dark.png').resize((20,20),)
image_dark_tk = ImageTk.PhotoImage(dark_image)

# Importing image for icon for ctk.CTkButton
image_ctk = ctk.CTkImage(light_image=Image.open('python_dark.png'),
                         dark_image=Image.open('python_light.png'))

# Functions 
def fill_image(event):
    global resized_tk
    canvas_ratio = event.width / event.height

    if canvas_ratio > image_ratio:
        width = int(event.width)
        height = int(width / image_ratio)
    else:
        height = int(event.height)
        width = int(height * image_ratio)

    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(int(event.width/2), int(event.height/2), anchor ='center', image = resized_tk)
    canvas.create_text(200, 50, text='''Fill the canvas with image
maintaining aspect ratio''', fill='white', font=('Arial', 20))


def stretch_image(event):
    global resized_tk_strch
    width_strch = event.width
    height_strch =  event.height
    # Resize the image to fit in the canvas
    resized_image_strch = image_original.resize((width_strch,height_strch))
    resized_tk_strch = ImageTk.PhotoImage(resized_image_strch)
    canvas_demo.create_image(0,0, image=resized_tk_strch, anchor='nw')
    canvas_demo.create_text(100, 50, text='''Stretch image to 
fill the canvas''', fill='white', font=('Arial', 10))


def show_full_image(event):
    global resized_tk_shofllimg
    canvas_ratio = event.width / event.height

    if canvas_ratio > image_ratio:
        height_shofllimg = int(event.height)
        width_shofllimg = int(height_shofllimg / image_ratio)
    else:
        width_shofllimg = int(event.width)
        height_shofllimg = int(width_shofllimg * image_ratio)

    resized_image_shofllimg = image_original.resize((width_shofllimg, height_shofllimg))
    resized_tk_shofllimg = ImageTk.PhotoImage(resized_image_shofllimg)
    canvas_demo2.create_image(int(event.width/2), int(event.height/2), anchor ='center', image = resized_tk_shofllimg)
    canvas_demo2.create_text(100, 50, text='''Resize image to 
stay in the canvas''', fill='white', font=('Arial', 10))


# Funtion to toggle night mode
def toggle_nightmode():
    if ctk.get_appearance_mode() == 'Dark':
        ctk.set_appearance_mode('Light')
    else:
        ctk.set_appearance_mode('Dark')




# Frame for buttons
button_frame = ttk.Frame(wd)

# Different types of buttons
button = ttk.Button(button_frame, text='Toggle night mode', image = image_dark_tk, compound = 'left', command=toggle_nightmode)
button.pack()

buttonCtk1 = ctk.CTkButton(button_frame, text='A Button', image = image_dark_tk, compound = 'left')
buttonCtk1.pack(pady = 5)

buttonCtk2 = ctk.CTkButton(button_frame, text='A Button', image = image_ctk, compound = 'left')
buttonCtk2.pack(pady = 5)

button_frame.grid(column=0, row=0, rowspan=1, sticky='nsew')

# Canvas
canvas = tk.Canvas(wd, background='red', bd=0, highlightthickness=0,relief='ridge')
canvas.grid(column=1, columnspan=3, row=0, rowspan=2, sticky='nsew')
canvas.bind('<Configure>', fill_image)

# A demo canvas
canvas_demo = tk.Canvas(button_frame, background='blue', bd=10, highlightthickness=10,relief='ridge')
canvas_demo.pack()
canvas_demo.bind('<Configure>', stretch_image)

canvas_demo2 = tk.Canvas(button_frame, background='red', bd=10, highlightthickness=10,relief='ridge')
canvas_demo2.pack()
canvas_demo2.bind('<Configure>', show_full_image)


wd.mainloop()