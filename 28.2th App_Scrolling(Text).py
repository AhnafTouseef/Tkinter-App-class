import tkinter as tk
from tkinter import ttk
from random import randint, choice

# setup
window = tk.Tk()
x, y = 400, 400
window.geometry(f'{x}x{y}')
window.title('Scrolling')
  
text = tk.Text(window, wrap='word', font=('Arial', 12))
for i in range (200):
    text.insert(f'{i}.0', f'text {i}\n')
text.pack(fill='both', expand=True)

scrollbarY = ttk.Scrollbar(window, orient='vertical', command=text.yview)
text.config(yscrollcommand=scrollbarY.set)
scrollbarY.place(relx=1, rely=0, relheight=1, anchor='ne')


# run window
window.mainloop()