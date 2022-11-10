import tkinter as tk
from PIL import ImageTk
from tkinter import filedialog
import zoom

class CustomImage():
    def __init__(self,data,name,pure_path):
        self.data = data
        self.name = name
        self.pure_path = pure_path

    def get_data(self):
        return self.name


class Gallery():
    def __init__(self, master, ok_button_command, images = []):
        self.master = master

        self.export_file = ""
        self.images = images
        self.current = 0

        self.label = tk.Label(self.master, compound=tk.TOP)
        self.label.pack()

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        tk.Button(self.frame, text="Добавить", command=self.add_image).pack(side=tk.LEFT)
        tk.Button(self.frame, text='<---', command=lambda: self.move(-1)).pack(side=tk.LEFT)
        tk.Button(self.frame, text='--->', command=lambda: self.move(+1)).pack(side=tk.LEFT)
        tk.Button(self.frame, text='Zoom', command=self.zoom_fun).pack(side=tk.LEFT)
        tk.Button(self.frame, text='Ок', command=ok_button_command).pack(side=tk.LEFT)
        tk.Button(self.frame, text='Выход', command=self.exit).pack(side=tk.LEFT)
        self.added_images()
        self.move(0)

    def move(self,delta):
        if not (0 <= self.current + delta < len(self.images)):
            return
        self.current += delta
        try:
            photo = ImageTk.PhotoImage(data=self.images[self.current].data, format="jpg")
        except:
            photo = ImageTk.PhotoImage(data=self.images[self.current].data, format="png")
        self.label['text'] = self.images[self.current].name
        self.label['image'] = photo
        self.label.photo = photo

    def add_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image File", ('.png','.jpg')),])
        print(path)
        with open(path, "rb") as file:
            self.images.append(CustomImage(file.read(), path.split("/")[-1], path))
        self.move(0)

    def added_images(self):
        self.old_images = self.images
        self.images = []
        for i in range(len(self.old_images)):
            self.images.append(CustomImage(self.old_images[i][0], self.old_images[i][1], self.old_images[i][2]))

    def zoom_fun(self):
        path = self.images[self.current].pure_path
        window = tk.Toplevel(self.master)
        app = zoom.Zoom_Advanced(window, path=path)

    def exit(self):
        self.master.destroy()