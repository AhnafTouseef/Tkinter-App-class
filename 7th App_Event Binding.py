import tkinter as tk
from tkinter import ttk

def get_pos_on_window(event):
    print(f'windoX:{event.x} windowY{event.y}')

def get_pos_on_button(event):
    print(f'buttonX:{event.x} buttonY{event.y}')

# setup 
wd = tk.Tk()
wd.title('Event Binding')
# wd.geometry('600x400')


# widget 
text = tk.Text(wd)
text.pack()

entry = ttk.Entry(wd)
entry.pack()

button = ttk.Button(wd, text='A button')
button.pack()

# events 
wd.bind('<Alt-KeyPress-a>', lambda event: print('A was pressed with alt'))
button.bind('<Alt-KeyPress-s>', lambda event: print('S was pressed with alt'))
wd.bind('<KeyPress>', lambda event: print(f'A button was pressed ({event.char})'))

wd.bind('<Motion>', get_pos_on_window)
button.bind('<Motion>', get_pos_on_button)

entry.bind('<FocusIn>', lambda event: print('entry field was slected'))
entry.bind('<FocusOut>', lambda event: print('entry field was unslected'))

# Exercise 
text.bind('<Shift-MouseWheel>', lambda event: print('Mousewheel with shift'))



# run 
wd.mainloop()