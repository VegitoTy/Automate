import tkinter as tk
import os
import json
import multiprocessing

def exe_algorithm(file):

    with open('./data.json', 'r+') as e:
        data = json.load(e)
        data["Executables"].append(file)
        e.seek(0)
        json.dump(data, e, indent=4)
        e.truncate()

    global root
    root = tk.Tk()
    root.title("Automate")

    root.attributes('-topmost', True)
    root.update()

    Label = tk.Label(root, text=f'Select what do you want to do with {file}')
    Label.pack()

    OpenButton = tk.Button(root, text='Open', command=lambda: open1(file))
    OpenButton.pack()

    OpenDeleteButton = tk.Button(root, text='Open and Delete', command=lambda: opendel(file))
    OpenDeleteButton.pack()

    Delete = tk.Button(root, text='Delete', command=lambda: delete(file))
    Delete.pack()

    Cancel = tk.Button(root, text='Cancel', command=root.destroy)
    Cancel.pack()

    root.mainloop()

def open1(file):
    file_run = multiprocessing.Process(target=os.system, args=[f'"{file}"'])
    file_run.start()
    root.destroy()

def open_del_process(file):
    os.system(f'"{file}"')
    os.remove(file)
# not much going on here
def opendel(file):
    file_run = multiprocessing.Process(target=open_del_process, args=[file])
    file_run.start()
    root.destroy()

def delete(file):
    os.remove(file)
    root.destroy()