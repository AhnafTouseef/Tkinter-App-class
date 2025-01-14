import tkinter as tk
from tkinter import ttk
from random import choice

# setup
window = tk.Tk()
x, y = 400, 400
window.geometry(f'{x}x{y}')
window.title('Scrolling')

table = ttk.Treeview(window, columns=(1,2), show='headings')
table.heading(1, text='First name')
table.heading(2, text='Last name')
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Kenny', 'Taylor', 'Anna', 'Lisa']
last_names = ['Smith','Brown','Wilson','Thompson','Cook','Taylor','Walker','Clark']
for i in range(100):
    table.insert(parent='', index='end', values=(choice(first_names), choice(last_names)))
table.pack(expand=True, fill='both')

scrollbar = ttk.Scrollbar(window, orient='vertical', command=table.yview)
table.configure(yscrollcommand=scrollbar.set)
scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')




# run window
window.mainloop()