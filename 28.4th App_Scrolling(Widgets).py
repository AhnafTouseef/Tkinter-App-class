import tkinter as tk
from tkinter import ttk

class ListFrame(ttk.Frame):
    def __init__(self, parent, text_data, item_height):
        super().__init__(parent)
        self.pack(expand=True, fill='both')

        # Widget data
        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number * item_height

        # canvas
        self.canvas = tk.Canvas(self,background='red', scrollregion=(0,0,self.winfo_width(),self.list_height))
        self.canvas.pack(fill='both', expand=True)

        # Display frame
        self.frame = ttk.Frame(self)
        
        for index, item in enumerate(self.text_data):
            self.create_item(index, item).pack(expand=True, fill='both', padx=4, pady=10)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        # event 
        self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta/60), 'units'))
        self.bind('<Configure>', self.update_size)

    def update_size(self, event):
        if self.list_height >= self.winfo_height():
            height = self.list_height
            self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta/60), 'units'))
            self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')


        else:
            height = self.winfo_height()
            self.canvas.unbind_all('<MouseWheel>')
            self.scrollbar.place_forget()

        self.canvas.create_window((0,0),
                                   window=self.frame, 
                                   anchor='nw', 
                                   width=self.winfo_width(), 
                                   height=height)

    def create_item(self, index, item):
        frame = ttk.Frame(self.frame)

        # Grid Layout
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure((0,1,2,3,4), weight=1, uniform='a')

        # Widgets
        ttk.Label(frame, text = f'#{index}').grid(row=0, column=0)
        ttk.Label(frame, text = item[0]).grid(row=0, column=1)
        ttk.Button(frame, text = item[1]).grid(row=0, column=2, columnspan=3, sticky='nsew')

        return frame


# setup
window = tk.Tk()
x, y = 500, 400
window.geometry(f'{x}x{y}')
window.title('Scrolling')

text_list = [('label','button'),('thing','click'),('third','something'),('label1','button'),('label2','button'),('label3','button'),('label4','button')]
list_frame = ListFrame(window, text_list, 100)




# run window
window.mainloop()
