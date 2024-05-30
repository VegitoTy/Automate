import tkinter as tk
import os
import multiprocessing
import shutil

def apk_algorithm(file):

    global root
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Automate")

    root.attributes("-topmost", True)
    root.update()

    name = os.path.basename(file).split('/')[-1]

    Label = tk.Label(root, text="Would you like to open this apk?")
    Label.pack()

    Label2 = tk.Label(root, text=name)
    Label2.pack()

    open1 = tk.Button(root, text="Open Apk", command=lambda: openapk(file))
    open1.pack()

    cancel1 = tk.Button(root, text="No", command=lambda: cancel(file))
    cancel1.pack()

    root.mainloop()

def openapk(file):
    name, extension = os.path.splitext(file)
    name = os.path.basename(file).split('/')[-1][:-len(extension)]

    count = len(name) + len(extension)

    move = f"{file[:-count]}APKs/{name}{extension}"

    while os.path.exists(move):
        move = f"{move[:-len(extension)]}1{extension}"

    shutil.move(file, move)

    open_process = multiprocessing.Process(target=os.system, args=[f'"{move}"'])
    open_process.start()

    root.destroy()

def cancel(file):
    name, extension = os.path.splitext(file)
    name = os.path.basename(file).split('/')[-1][:-len(extension)]

    count = len(name) + len(extension)

    move = f"{file[:-count]}APKs/{name}{extension}"

    while os.path.exists(move):
        move = f"{move[:-len(extension)]}1{extension}"

    shutil.move(file, move)

    root.destroy()