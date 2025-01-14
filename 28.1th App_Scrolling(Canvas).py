import tkinter as tk
from tkinter import ttk
from random import randint, choice

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Scrolling')

# canvas
canvas = tk.Canvas(window, bg='white', scrollregion=(0,0,2000,5000))
canvas.create_line(0,0,2000,5000, fill='red')

for i in range(100):
    l = randint(0, 2000)
    t = randint(0, 5000)
    r = l + randint(10, 500)
    b = t + randint(10, 500)
    color = choice(['red', 'green', 'blue', 'yellow', 'purple', 'orange'])
    canvas.create_rectangle(l,t,r,b, fill=color)

canvas.pack(fill='both', expand=True)

# Mousewheel scrolling
canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-1*(event.delta//120), 'units'))
# Mouse scrolling to left and right holding ctrl key
canvas.bind('<Control-MouseWheel>', lambda event: canvas.xview_scroll(-1*(event.delta//120), 'units'))

# scrollbar
scrollbarY = ttk.Scrollbar(window, orient='vertical', command=canvas.yview)
canvas.config(yscrollcommand=scrollbarY.set)
scrollbarY.place(relx=1, rely=0, relheight=1, anchor='ne')

scrollbarX = ttk.Scrollbar(window, orient='horizontal', command=canvas.xview)
canvas.config(xscrollcommand=scrollbarX.set)
scrollbarX.place(relx=0, rely=1, relwidth=1, anchor='sw')


# run window
window.mainloop()