import tkinter as tk
from tkinter import ttk
from random import choice

# setup 
wd = tk.Tk()
wd.geometry('600x400')
wd.title('Treeview')

# Data 
First_name = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_name = ['Smith', 'Brown', 'Wilson', 'Thomas', 'Cook', 'Henry', 'Taylor', 'Walker', 'Clark']

# Treeview 
table =  ttk.Treeview(wd, columns=('first', 'last', 'email'), show='headings')
table.heading('first', text = 'Fiest name')
table.heading('last', text = 'Surname')
table.heading('email', text = 'email')
table.pack(fill='both', expand=True)

# Insert value in table 
# table.insert(parent='', index=0, values=('John', 'Doe', 'johndoe@gmail.com'))
for i in range(100):
    First= choice(First_name)
    last = choice(last_name)
    email = f'{First.lower()}{last.lower()}@{choice(['gmail.com', 'yahoo.com', 'msn.com'])}'
    data = (First, last, email)
    table.insert(parent='', index=0, values=data)

table.insert(parent='', index=0, values=('QQQQQQQQ', 'WWWWWWW', 'EEEEEEE'))
table.insert(parent='', index=4, values=('AAAAAAA', 'SSSSSSS', 'DDDDDDD'))
table.insert(parent='', index=tk.END, values=('AAAAAAAA', 'SSSSSSSS', 'DDDDDDD'))

# Events 
def item_select(_):
    # print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])

def delete_item(_):
    for i in table.selection():
        table.delete(i)


# table.bind('<<TreeviewSelect>>', lambda event: print(table.selection()))
table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_item)

# Item


# run 
wd.mainloop()