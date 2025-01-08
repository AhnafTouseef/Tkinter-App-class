import tkinter as tk
from tkinter import ttk

# setup 
wd = tk.Tk()
wd.geometry('600x400')
wd.title('Canvas')

# canvas 
canvas = tk.Canvas(wd, bg = 'white')
canvas.pack()

canvas.create_rectangle((50,20,100,100), fill = 'red', width=5, outline='green')
canvas.create_oval((200,0,300,100), fill = 'green')
canvas.create_arc((200,0,300,100), fill = 'red', start=45, extent=140, style=tk.CHORD, outline='yellow', width=10)
canvas.create_line((0,0,100,150), fill = 'blue')
canvas.create_polygon((0,0,50,50, 200,50, 150,-50), fill = 'gray')
canvas.create_text((100,200), text = 'this is some text', angle=45, fill='#bab2f4')

canvas.create_window((150,200), window=ttk.Button(wd, text='This is text in a canvas'))

# Exercise 
def draw_on_canvas(event):
    x=event.x
    y=event.y
    canvas.create_oval((x-brush_size/2, y-brush_size/2, x+brush_size/2, y+brush_size/2), fill='black')
    pass

def brush_size_adjust(event):
    global brush_size
    if event.delta <0:
        brush_size+=1
    else:
        brush_size -=1
    brush_size = max(0, min(brush_size, 50))

brush_size=2
canvas.bind('<Motion>', draw_on_canvas)
canvas.bind('<MouseWheel>', brush_size_adjust)


# run 
wd.mainloop()
