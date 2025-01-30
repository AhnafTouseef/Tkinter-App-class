import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.widgets import DateEntry

#window
wd = ttk.Window(themename='darkly')
wd.title('Extra widget')
x, y = 500,500
# wd.geometry(f'{x}x{y}')

#scrollable frame
scroll_frame = ScrolledFrame(wd)
scroll_frame.pack(expand=True, fill= 'both')

for i in range(100):
    ttk.Label(scroll_frame, text=f'Label {i}').pack()
    ttk.Button(scroll_frame, text=f'Button {i}').pack()

#toast
toast = ToastNotification(title='This is messege title',
                          message= 'This is the actual messege',
                          duration= 2000,
                          bootstyle = 'dark',
                          position = (30,50,'ne'))

ttk.Button(wd, text='Show toast', 
           command=toast.show_toast,
           ).pack()

# Tooltip
button = ttk.Button(wd, text = 'tooltip button', bootstyle = 'wraning')
button.pack(pady=10)
ToolTip(button, text='This does something', bootstyle='danger-inverse')


#calendar
calendar = DateEntry(wd)
calendar.pack(pady=10)
ttk.Button(wd, text='Get calendar date', command= lambda: print(calendar.entry.get())).pack()

#Progres
progress_int = tk.IntVar(value=50)
progress = ttk.Floodgauge(wd, 
                          text='Progress', 
                          variable=progress_int,
                          bootstyle='danger',
                          mask='mask {}%')
progress.pack(pady=10, fill='x')
ttk.Scale(wd, from_=0, to=100, variable=progress_int).pack(fill='x')

# Meter
meter = ttk.Meter(wd,
                  amounttotal= 100,
                  amountused= 10,
                  interactive=1,
                  metertype='semi',
                  subtext= 'Some text',
                  bootstyle='danger')
meter.pack()

#run
wd.mainloop()