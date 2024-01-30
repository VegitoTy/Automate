import pillow_avif
from pillow_heif import register_heif_opener
from PIL import Image, ImageTk
import os
import tkinter as tk
import shutil

def convert_jpg(file):

    name, extension = os.path.splitext(file)

    if extension == ".jpg":
        name = os.path.basename(file).split('/')[-1][:-len(extension)]

        count = len(name) + len(extension)

        exists = f"{file[:-count]}Images/{name}{extension}"

        if not os.path.exists(exists):
            shutil.move(file, f"{file[:-count]}Images/{name}{extension}")
        else:
            while os.path.exists(exists):
                exists = f"{exists[:-len(extension)]}1{extension}" # dumb way to deal with already exists errors
            shutil.move(file, exists)
        
        return

    register_heif_opener()

    image1 = Image.open(file)

    global root
    root = tk.Tk()
    root.title("Automate")
    root.geometry("800x600")

    root.attributes('-topmost', True)
    root.update()

    image = ImageTk.PhotoImage(image1)

    Label = tk.Label(root, text=f'Convert this to jpg?')
    Label.pack()

    frame = tk.Frame(root, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    label = tk.Label(frame, image = image)
    label.pack()

    ConvertButton = tk.Button(root, text='Convert', command=lambda: convert(file))
    ConvertButton.pack()

    NoButton = tk.Button(root, text="No", command=lambda: no(file))
    NoButton.pack()

    root.mainloop()

def convert(file):
    image = Image.open(file)
    rgb_im = image.convert("RGB")
    name, extension = os.path.splitext(file)
    name = os.path.basename(file).split('/')[-1][:-len(extension)]

    count = len(name) + len(extension)

    exists = f"{file[:-count]}Images/{name}.jpg"

    if not os.path.exists(exists):
        rgb_im.save(exists)
    else:
        while os.path.exists(exists):
            exists = f"{exists[:-4]}1.jpg"
        rgb_im.save(exists)

    os.remove(file)

    root.destroy()

def no(file):
    name, extension = os.path.splitext(file)
    name = os.path.basename(file).split('/')[-1][:-len(extension)]

    count = len(name) + len(extension)

    exists = f"{file[:-count]}Images/{name}{extension}"

    if not os.path.exists(exists):
        shutil.move(file, f"{file[:-count]}Images/{name}{extension}")
    else:
        while os.path.exists(exists):
            exists = f"{exists[:-len(extension)]}1{extension}"
        shutil.move(file, exists)

    root.destroy()