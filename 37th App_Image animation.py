import customtkinter as ctk
from PIL import Image
from os import walk

class AnimatedButton(ctk.CTkButton):
    def __init__(self, parent, light_path, dark_path):
        self.frames = self.import_folders(light_path, dark_path)
        self.frame_index = 0
        self.animation_lenght = len(self.frames) - 1
        self.animation_status = ctk.StringVar(value = 'start')
        self.animation_status.trace('w', self.animate)

        super().__init__(master=parent, text="A animated Button",
                         image = self.frames[self.frame_index], command= self.trigger_animation)
        self.pack(expand=True)

    def import_folders(self, light_path, dark_path):
        image_paths = []
        for path in (light_path, dark_path):
            for _, __, image_data in walk(path):
                sorted_data = sorted(image_data,
                                     key= lambda item: int(item.split('.')[0][-5:]))
                full_data_path = [path + '/' + item for item in sorted_data]
                image_paths.append(full_data_path) 
        image_paths = zip(*image_paths)

        ctk_images = []
        for image_path in image_paths:
            ctk_image = ctk.CTkImage(light_image = Image.open(image_path[0]),
                                     dark_image= Image.open(image_path[1])) 
            ctk_images.append(ctk_image)
        return ctk_images

    def trigger_animation(self):
        if self.animation_status.get() == 'start':
            self.frame_index = 0
            self.animation_status.set('forward')
        if self.animation_status.get() == 'end':
            self.frame_index = self.animation_lenght
            self.animation_status.set('backward')

    def animate(self, *args):
        if self.animation_status.get() == 'forward':
            self.frame_index += 1
            self.configure(image = self.frames[self.frame_index])
            if self.frame_index < self.animation_lenght:
                self.after(20, self.animate)
            else:
                self.animation_status.set('end')

        elif self.animation_status.get() == 'backward':
            self.frame_index -= 1
            self.configure(image = self.frames[self.frame_index])
            if self.frame_index > 0:
                self.after(20, self.animate)
            else:
                self.animation_status.set('start')



wd = ctk.CTk()
wd.geometry("300x200")
wd.title("Image Animation")
ctk.set_appearance_mode("dark")

def toggle_nightmode():
    if ctk.get_appearance_mode() == 'Dark':
        ctk.set_appearance_mode('Light')
    else:
        ctk.set_appearance_mode('Dark')
button = ctk.CTkButton(wd, text='Toggle night mode', compound = 'left', command=toggle_nightmode)
button.pack()

AnimatedButton(wd, 'light', 'dark')


wd.mainloop()