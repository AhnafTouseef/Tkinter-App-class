import tkinter as tk
from tkinter import ttk

class ListFrame(ttk.Frame):
    def __init__(self, parent, text_data, item_height):
        super().__init__(parent)
        self.pack(expand=True, fill='both')

        # Widget data
        self.text_data = text_data
        self.item_number = len(text_data)
        self.item_height = self.item_number * item_height

        # canvas
        self.canvas = tk.Canvas(self,background='red', scrollregion=(0,0,500,self.item_height))
        self.canvas.pack(fill='both', expand=True)

        # Display frame
        self.frame = ttk.Frame(self)
        
        for index, item in enumerate(self.text_data):
            self.create_item(index, item).pack(expand=True, fill='both', padx=5, pady=5)

        self.canvas.create_window((0,0), window=self.frame, anchor='nw', width=500, height=self.item_height)

        # event 
        self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta/120), 'units'))

    def create_item(self, index, item):
        frame = ttk.Frame(self.frame)

        # Grid Layout
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure((0,1,2,3,4), weight=1, uniform='a')

        # Widgets
        ttk.Label(frame, text = f'#{index}').grid(row=0, column=0, sticky='nsew')
        ttk.Label(frame, text = item[0]).grid(row=0, column=1, sticky='nsew')
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