import tkinter as tk
from torrentool.api import Torrent
import hurry.filesize
import os
import multiprocessing
import shutil

def torrent_algorithm(file):

    global root
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Automate")

    root.attributes("-topmost", True)
    root.update()

    Label = tk.Label(root, text="Would you like to open this torrent?")
    Label.pack()

    torrent = Torrent.from_file(file)

    name = tk.Label(root, text=f"{torrent.name}")
    name.pack()

    size = tk.Label(root, text=hurry.filesize.size(torrent.total_size))
    size.pack()

    open1 = tk.Button(root, text="Open Torrent", command=lambda: opentorrent(file))
    open1.pack()

    cancel1 = tk.Button(root, text="No", command=lambda: cancel(file))
    cancel1.pack()

    root.mainloop()

def opentorrent(file):
    name, extension = os.path.splitext(file)
    name = os.path.basename(file).split('/')[-1][:-len(extension)]

    count = len(name) + len(extension)

    move = f"{file[:-count]}/Torrents/{name}{extension}"

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

    move = f"{file[:-count]}/Torrents/{name}{extension}"

    while os.path.exists(move):
        move = f"{move[:-len(extension)]}1{extension}"

    shutil.move(file, move)

    root.destroy()