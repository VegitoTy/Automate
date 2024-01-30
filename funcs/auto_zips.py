import tkinter as tk
import os
import multiprocessing
from tkinter import filedialog
import shutil

def zip_algorithm(file):
    
    name, extension = os.path.splitext(file)
    name = os.path.basename(file).split('/')[-1][:-len(extension)]

    global root
    root = tk.Tk()
    root.title("Automate")

    root.attributes("-topmost", True)
    root.geometry("800x600")
    root.update()

    heading = tk.Label(root, text=f"What would you like to do with {name}{extension}", pady=20)
    heading.pack()

    open = tk.Button(root, text="Open", command=lambda: _open(file))
    open.pack()

    open_and_delete = tk.Button(root, text="Open And Delete", command=lambda: _open_and_delete(file))
    open_and_delete.pack()

    move_and_open = tk.Button(root, text="Move and Open", command=lambda: _move_and_open(file))
    move_and_open.pack()

    move_to = tk.Button(root, text="Move To..", command=lambda: _move_to(file))
    move_to.pack()

    nothing = tk.Button(root, text="Nothing", command=lambda: _nothing(file))
    nothing.pack()

    root.mainloop()

def _open(file):
    name, extension = os.path.splitext(file)
    name = os.path.basename(file).split('/')[-1][:-len(extension)]

    count = len(name) + len(extension)

    move = f"{file[:-count]}Compressed/{name}{extension}"

    while os.path.exists(move):
        move = f"{move[:-len(extension)]}1{extension}"

    shutil.move(file, move)

    run = multiprocessing.Process(target=os.system, args=[f'"{move}"'])
    run.start()

    root.destroy()

def open_delete_process(file):
    os.system(f'"{file}"')
    os.remove(file)

def _open_and_delete(file):
    run = multiprocessing.Process(target=open_delete_process, args=[file])
    run.start()

    root.destroy()

def _move_and_open(file):
    name, extension = os.path.splitext(file)
    name = os.path.basename(file).split('/')[-1][:-len(extension)]

    directoy = filedialog.askdirectory()

    move = f"{directoy}/{name}{extension}"

    while os.path.exists(move):
        move = f"{move[:-len(extension)]}1{extension}"

    shutil.move(file, move)

    run = multiprocessing.Process(target=os.system, args=[f'"{move}"'])
    run.start()

    root.destroy()

def _move_to(file):
    name, extension = os.path.splitext(file)
    name = os.path.basename(file).split('/')[-1][:-len(extension)]

    directory = filedialog.askdirectory()

    move = f"{directory}/{name}{extension}"

    while os.path.exists(move):
        move = f"{move[:-len(extension)]}1{extension}"

    shutil.move(file, move)

    root.destroy()

def _nothing(file):
    name, extension = os.path.splitext(file)
    name = os.path.basename(file).split('/')[-1][:-len(extension)]

    count = len(name) + len(extension)

    move = f"{file[:-count]}Compressed/{name}{extension}"

    while os.path.exists(move):
        move = f"{move[:-len(extension)]}1{extension}"

    shutil.move(file, move)

    root.destroy()