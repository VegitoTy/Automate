import tkinter as tk
import os
import multiprocessing
from tkinter import filedialog
import shutil
from tkinter import messagebox
import comtypes.client

def pdf_algorithm(file):
    
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

    move_and_open = tk.Button(root, text="Move and Open", command=lambda: _move_and_open(file))
    move_and_open.pack()

    move_to = tk.Button(root, text="Move To..", command=lambda: _move_to(file))
    move_to.pack()

    nothing = tk.Button(root, text="Nothing", command=lambda: _nothing(file))
    nothing.pack()

    root.mainloop()

def PPTtoPDF(inputFileName, outputFileName):
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application") # plz tell a better way for converting to pdf
    powerpoint.Visible = 1
    deck = powerpoint.Presentations.Open(inputFileName)
    deck.ExportAsFixedFormat(outputFileName, 2)
    deck.Close()
    powerpoint.Quit()
    os.remove(inputFileName)

def _open(file):
    name, extension = os.path.splitext(file)
    name = os.path.basename(file).split('/')[-1][:-len(extension)]

    count = len(name) + len(extension)

    move = f"{file[:-count]}PDFs/{name}{extension}"

    if extension.lower() != ".pdf":
        message = messagebox.askyesno("Automate", "Convert to PDF?")

        if message:
            move = f"{move[:-len(extension)]}.pdf"
            while os.path.exists(move):
                move = f"{move[:-4]}1.pdf"
            try:
                PPTtoPDF(file, move)
            except:
                return messagebox.showerror("Automate", "Couldn't convert to PDF, Make sure you have powerpoint installed!")
        else:
            shutil.move(file, move)
    else:
        shutil.move(file, move)

    run = multiprocessing.Process(target=os.system, args=[f'"{move}"'])
    run.start()

    root.destroy()

def _move_and_open(file):
    name, extension = os.path.splitext(file)
    name = os.path.basename(file).split('/')[-1][:-len(extension)]

    directory = filedialog.askdirectory()

    move = f"{directory}/{name}{extension}"

    if extension.lower() != ".pdf":
        message = messagebox.askyesno("Automate", "Convert to PDF?")

        if message:
            move = f"{move[:-len(extension)]}.pdf"
            while os.path.exists(move):
                move = f"{move[:-4]}1.pdf"
            try:
                PPTtoPDF(file, move)
            except:
                return messagebox.showerror("Automate", "Couldn't convert to PDF, Make sure you have powerpoint installed!")
        else:
            shutil.move(file, move)
    else:
        shutil.move(file, move)

    run = multiprocessing.Process(target=os.system, args=[f'"{move}"'])
    run.start()

    root.destroy()

def _move_to(file):
    name, extension = os.path.splitext(file)
    name = os.path.basename(file).split('/')[-1][:-len(extension)]

    directory = filedialog.askdirectory()

    move = f"{directory}/{name}{extension}"

    if extension.lower() != ".pdf":
        message = messagebox.askyesno("Automate", "Convert to PDF?")

        if message:
            move = f"{move[:-len(extension)]}.pdf"
            while os.path.exists(move):
                move = f"{move[:-4]}1.pdf"
            try:
                PPTtoPDF(file, move)
            except:
                return messagebox.showerror("Automate", "Couldn't convert to PDF, Make sure you have powerpoint installed!")
            return root.destroy()
    
    while os.path.exists(move):
        move = f"{move[:-4]}1{extension}"
    shutil.move(file, move)

    root.destroy()

def _nothing(file):
    name, extension = os.path.splitext(file)
    name = os.path.basename(file).split('/')[-1][:-len(extension)]

    count = len(name) + len(extension)

    move = f"{file[:-count]}PDFs/{name}{extension}"

    if extension.lower() != ".pdf":
        message = messagebox.askyesno("Automate", "Convert to PDF?")

        if message:
            move = f"{move[:-len(extension)]}.pdf"
            while os.path.exists(move):
                move = f"{move[:-4]}1.pdf"
            try:
                PPTtoPDF(file, move)
            except:
                return messagebox.showerror("Automate", "Couldn't convert to PDF, Make sure you have powerpoint installed!")
            return root.destroy()
        
    while os.path.exists(move):
        move = f"{move[:-4]}1{extension}"
    shutil.move(file, move)

    root.destroy()