import ttkbootstrap as ttk

# setup 
wd = ttk.Window(themename='journal')
wd.title('ttk bootstrap intro')
x, y = 400,400
wd.geometry(f'{x}x{y}')


label= ttk.Label(wd, text='Label')
label.pack(pady=10)

button1 = ttk.Button(wd, text='red', bootstyle='danger-outline')
button1.pack(pady=10)

button2 = ttk.Button(wd, text='Warning', bootstyle= 'warning')
button2.pack(pady=10)

button3 = ttk.Button(wd, text='Green', bootstyle='success-outline')
button3.pack(pady=10)

# run 
wd.mainloop()