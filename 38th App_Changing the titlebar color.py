import customtkinter as ctk
from ctypes import windll, byref, sizeof, c_int


wd = ctk.CTk(fg_color='#ffccff')
wd.geometry("500x400")
wd.title("Changing the titlebar color")

HWND = windll.user32.GetParent(wd.winfo_id())
titlebar_color  = 0x003996AA # color format style: 0x00BBGGRR (BGR format)
title_coclor = 0x00FD9639
windll.dwmapi.DwmSetWindowAttribute(HWND,
                                    35, 
                                    byref(c_int(titlebar_color)),
                                    sizeof(c_int))

windll.dwmapi.DwmSetWindowAttribute(HWND,
                                    36, 
                                    byref(c_int(title_coclor)),
                                    sizeof(c_int))


wd.mainloop()