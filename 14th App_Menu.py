import tkinter as tk
from tkinter import ttk

# setup 
wd = tk.Tk()
wd.geometry('600x400')
wd.title('Menu')

# Menu 
menu = tk.Menu(wd)

# Sub menu
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label='New', command= lambda: print('New file'))
file_menu.add_separator()
file_menu.add_command(label='Open', command= lambda: print('Open file'))
menu.add_cascade(label= 'File', menu=file_menu)

# another sub menu 
help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(label='Help entry', command= lambda: print(help_check_string.get()))
help_check_string = tk.StringVar(value='Help')
help_menu.add_checkbutton(label='Check it', onvalue='on', offvalue='off', variable=help_check_string)
menu.add_cascade(label= 'Help', menu=help_menu)

# exrcise 
exercise_menu = tk.Menu(menu, tearoff=False)
exercise_menu.add_command(label='Exercise test 1')
menu.add_cascade(label='Exercise', menu = exercise_menu )

exercise_sub_menu = tk.Menu(menu, tearoff=False)
exercise_sub_menu.add_command(label='Exercise test 2')
exercise_menu.add_cascade(label='Exrecise 1' ,menu=exercise_sub_menu)


wd.configure(menu = menu)

# Menu button
menu_button = ttk.Menubutton(wd, text='Menu Button')
menu_button.pack()

button_sub_menu = tk.Menu(menu_button, tearoff=False)
button_sub_menu.add_command(label='Entry 1', command= lambda: print('test 1'))
button_sub_menu.add_checkbutton(label='Check 1')
menu_button.configure(menu=button_sub_menu)


# run 
wd.mainloop()