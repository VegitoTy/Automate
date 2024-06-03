import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import json
import App
import pathlib
from pynput import keyboard

class GUI:

    def __init__(self, root):

        root.title("Automate")
        root.geometry("800x600")
        
        ft = tkFont.Font(family='Times', size=38)

        settings_label=tk.Label(root, text="Settings", font=ft)
        settings_label.pack()

        with open("./settings.json", "r+") as e:
            settings = json.load(e)

            auto_exe = 0
            auto_jpg = 0
            auto_apk = 0
            auto_torrent = 0
            auto_zips = 0
            auto_jars = 0
            auto_pdfs = 0
            auto_apps = 0
            voice_commands = 0

            if settings["auto_exe"]:
                auto_exe = 1
            if settings["auto_jpg"]:
                auto_jpg = 1
            if settings["auto_apk"]:
                auto_apk = 1
            if settings["auto_torrent"]:
                auto_torrent = 1
            if settings["auto_zips"]:
                auto_zips = 1
            if settings["auto_jars"]:
                auto_jars = 1
            if settings["auto_pdfs"]:
                auto_pdfs = 1
            if settings["auto_apps"]:
                auto_apps = 1
            if settings["voice_commands"]:
                voice_commands = 1

            self.auto_exe_var = tk.IntVar(value=auto_exe)
            self.auto_jpg_var = tk.IntVar(value=auto_jpg)
            self.auto_apk_var = tk.IntVar(value=auto_apk)
            self.auto_torrent_var = tk.IntVar(value=auto_torrent)
            self.auto_zips_var = tk.IntVar(value=auto_zips)
            self.auto_jars_var = tk.IntVar(value=auto_jars)
            self.auto_pdfs_var = tk.IntVar(value=auto_pdfs)
            self.auto_apps_var = tk.IntVar(value=auto_apps)
            self.voice_commands_var = tk.IntVar(value=voice_commands)

        ft = tkFont.Font(family='Times', size=18)

        self.apps = tk.Button(root, text="Choose Apps For Auto Exe", font=ft, justify="center", command=self.app_func)
        self.apps.pack()

        self.cmds = tk.Button(root, text="Configure Voice Commands", font=ft, justify="center", command=self.cmd_func)
        self.cmds.pack()

        self.voice_commands=tk.Checkbutton(root, text="Voice Commands", font=ft, justify="center", variable=self.voice_commands_var)
        self.voice_commands.pack()

        self.auto_exe=tk.Checkbutton(root, text="Auto Exe", font=ft, justify="center", variable=self.auto_exe_var)
        self.auto_exe.pack()
                                     
        self.auto_jpg=tk.Checkbutton(root, text="Auto JPG", justify="center", font=ft, variable=self.auto_jpg_var)
        self.auto_jpg.pack()

        self.auto_apk=tk.Checkbutton(root, text="Auto APK", font=ft, justify="center", variable=self.auto_apk_var)
        self.auto_apk.pack()

        self.auto_torrent=tk.Checkbutton(root, text="Auto Torrent", font=ft, justify="center", variable=self.auto_torrent_var)
        self.auto_torrent.pack()

        self.auto_zips=tk.Checkbutton(root, text="Auto Zips", font=ft, justify="center", variable=self.auto_zips_var)
        self.auto_zips.pack()

        self.auto_jars=tk.Checkbutton(root, text="Auto Jars", font=ft, justify="center", variable=self.auto_jars_var)
        self.auto_jars.pack()

        self.auto_pdfs=tk.Checkbutton(root, text="Auto PDFs", font=ft, justify="center", variable=self.auto_pdfs_var)
        self.auto_pdfs.pack()

        self.auto_apps=tk.Checkbutton(root, text="Auto Apps", font=ft, justify="center", variable=self.auto_apps_var)
        self.auto_apps.pack()

        self.save = tk.Button(root, text="Save And Run", font=ft, justify="center", command=self.save_func)
        self.save.pack()

    def cmd_func(self):
        def add_app():
            ft = tkFont.Font(family='Times', size=10)

            def terminal():
                def save():
                    if not command_entry.get() or command_entry.get() == "" or not voice_entry.get() or voice_entry.get() == "": return messagebox.showerror("Voice Configuration", "Please Fill All Fields!")
                    with open("./data.json", "r+") as e:
                        data:dict = json.load(e)
                        doc = [voice_entry.get().lower(), "cmd", command_entry.get()]

                        if doc in data["voice_cmds"]:
                            return messagebox.showerror("Voice Configuarion", "Cannot Have Duplicates!")

                        data["voice_cmds"].append(doc)
                        e.seek(0)
                        json.dump(data, e)
                        e.truncate()
                    table.insert(parent='', index=tk.END, values=(voice_entry.get().lower(), "cmd", command_entry.get()))
                    top3.destroy()

                top2.destroy()
                top3 = tk.Toplevel(root)
                top3.geometry("375x125")
                top3.title("Terminal Command")
                frame3 = tk.Frame(top3)

                tk.Label(frame3, text="Voice To Recognize", font=ft).grid(row = 0, column = 0)
                voice_entry = tk.StringVar()
                tk.Entry(frame3, textvariable=voice_entry).grid(row = 0, column = 1)
                tk.Label(frame3, text="Terminal Command", font=ft).grid(row = 1, column = 0)
                command_entry = tk.StringVar()
                tk.Entry(frame3, textvariable=command_entry).grid(row = 1, column = 1)

                frame3.pack()

                tk.Button(top3, text="Save", command=save).pack()

            def shortcut():
                keys_pressed = []

                def stop_record():
                    if listener.is_alive():
                        listener.stop()

                    record_button.configure(text="Start Recording Shortcut", command=record_shortcut)

                def record_shortcut():
                    record_button.configure(text="Stop Recording", command=stop_record)

                    def on_press(key):
                        try:
                            name = key.char.upper()
                            keys_pressed.append(name)
                        except AttributeError:
                            name = key.name
                            if name == "cmd": return
                            keys_pressed.append(name)

                        text = shortcut_label.cget("text")
                        if text == "":
                            key_pressed_str = name
                        else:
                            key_pressed_str = f"{text} + {name}"

                        shortcut_label.configure(text=key_pressed_str)

                    global listener
                    listener = keyboard.Listener(on_press=on_press)
                    listener.start()

                def add_window():
                    keys_pressed.append("WIN")

                    text = shortcut_label.cget("text")

                    if text == "":
                        text += "WIN"
                    else:
                        text = f"{text} + WIN"

                    shortcut_label.configure(text=text)

                def save():
                    if not voice_entry.get() or voice_entry.get() == "": return messagebox.showerror("Voice Configuration", "Please Fill All Fields!")
                    if keys_pressed == []: return messagebox.showerror("Voice Configuration", "Record A Key Combination!")

                    with open("./data.json", "r+") as e:
                        data:dict = json.load(e)
                        doc = [voice_entry.get().lower(), "shortcut", keys_pressed]

                        if doc in data["voice_cmds"]: 
                            return messagebox.showerror("Voice Configuration", "Cannot Have Duplicates!")

                        data["voice_cmds"].append(doc)
                        e.seek(0)
                        json.dump(data, e)
                        e.truncate()
                    table.insert(parent='', index=tk.END, values=(voice_entry.get().lower(), "shortcut", shortcut_label.cget("text")))
                    top3.destroy()          

                def clear():
                    keys_pressed.clear()
                    shortcut_label.configure(text="")

                top2.destroy()
                top3 = tk.Toplevel(root)
                top3.geometry("375x125")
                top3.title("Windows Shortcut")
                frame3 = tk.Frame(top3)

                tk.Label(frame3, text="Voice To Recognize", font=ft).grid(row = 0, column = 0)
                voice_entry = tk.StringVar()
                tk.Entry(frame3, textvariable=voice_entry).grid(row = 0, column = 1)
                frame3.pack()

                tk.Button(top3, text="Add Windows Key", font=ft, justify="center", command=add_window).pack()

                shortcut_label = tk.Label(top3, text = "", font=ft, justify='center')
                shortcut_label.pack()

                record_button = tk.Button(top3, text = "Start Recording Shortcut", justify='center', command=record_shortcut)
                record_button.pack()

                frame4 = tk.Frame(top3)
                tk.Button(frame4, text="Clear", justify='center', command=clear).grid(row=0, column=0)
                tk.Button(frame4, text="Save", justify='center', command=save).grid(row=0, column=1)
                frame4.pack()

            top2 = tk.Toplevel(root)
            top2.geometry("375x125")
            top2.title("Add A Voice Command")
            tk.Label(top2, text="Select the type of function the voice command is gonna do.", font=ft).pack()

            frame2 = tk.Frame(top2)
            tk.Button(frame2, text="Windows Shortcut", command=shortcut, justify="center").grid(row = 0, column = 0)
            tk.Button(frame2, text="Terminal Command", command=terminal, justify="center").grid(row = 0, column = 1)
            frame2.pack()

        def remove_app():
            with open("./data.json", "r+") as e:
                data:dict = json.load(e)
                SelectList = table.selection()
                if not SelectList: return messagebox.showerror("Voice Recognition", "No Command Selected.")

                for command in SelectList:
                    i = 0
                    for saved in data["voice_cmds"]:
                        info = table.item(table.focus())["values"]
                        change = False
                        if saved[0].lower() == info[0].lower() and saved[1] == info[1]:
                            print("ok")
                            if info[1] == "cmd":
                                print("ok2")
                                if info[2] == saved[2]:
                                    change = True
                            else:
                                print("ok3")
                                shortcut_list = info[2].split(" + ")
                                print(shortcut_list)
                                print(saved[2])
                                if shortcut_list == saved[2]:
                                    change = True
                        
                        if change == True:
                            del data["voice_cmds"][i]
                            break
                        i += 1
                    table.delete(command)

                e.seek(0)
                json.dump(data, e)
                e.truncate()

        ft = tkFont.Font(family='Times', size=18)

        top = tk.Toplevel(root)
        top.geometry("750x250")
        top.title("Voice Commands Configuration")
        with open("./data.json") as e:
            data = json.load(e)
            current_cmds:dict = data["voice_cmds"]
            voices = []
            types = []
            commands = []
            for info in current_cmds:
                voices.append(info[0])
                types.append(info[1])
                string_val = info[2]
                if type(info[2]) == list:
                    string_val = ""
                    i = 1
                    for key in info[2]:
                        if len(info[2]) == i:
                            string_val += key.upper()
                            break
                        string_val += f"{key.upper()} + "
                        i += 1
                commands.append(string_val)
            table = ttk.Treeview(top, columns=("voice", "type", "command"), show="headings")
            table.heading('voice', text="Voice To Recognize")
            table.heading('type', text="Type Of Command")
            table.heading('command', text="Command")
            table.pack(expand=True)

            for i in range(len(voices)):
                data = (voices[i], types[i], commands[i])
                table.insert(parent='', index=tk.END, values=data)

            frame = tk.Frame(top)
            tk.Button(frame, text="Add", command=add_app, justify="center").grid(row = 0, column = 0)
            tk.Button(frame, text="Remove", command=remove_app, justify="center").grid(row = 0, column = 1)
            frame.pack()

    def app_func(self):
        def add_app():
            file_name = pathlib.Path(filedialog.askopenfilename(title="Select A Executable", filetypes=[("Executable", ".exe")])).name
            if file_name:
                with open("./data.json", "r+") as e:
                    data = json.load(e)
                    data["Apps"].append(file_name)
                    e.seek(0)
                    json.dump(data, e)
                    e.truncate()
            top.destroy()
            self.app_func()

        def remove_app():
            with open("./data.json", "r+") as e:
                data = json.load(e)
                SelectList = lb.curselection()
                if not SelectList: return messagebox.showerror("Auto Exe", "App Not Selected.")
                apps = [lb.get(i) for i in SelectList]
                for app in apps:
                    data["Apps"].remove(app)
                e.seek(0)
                json.dump(data, e)
                e.truncate()

            lb.delete(0, "end")
            current_apps.remove(app)
            for x in current_apps: lb.insert("end", x)

        ft = tkFont.Font(family='Times', size=18)

        top = tk.Toplevel(root)
        top.geometry("750x250")
        top.title("Add Or Remove Apps")
        with open("./data.json") as e:
            data = json.load(e)
            current_apps = []
            for exe in data["Apps"]:
                current_apps.append(exe)
            
            info_label = tk.Label(top, text="Select The App To Remove Or Click The Add Button To Add Some App", font=ft)
            info_label.pack()

            lb = tk.Listbox(top, selectmode="MULTIPLE", height=len(current_apps), width=200)
            for x in current_apps: lb.insert("end", x)
            lb.pack()

            tk.Button(top, text="Add", command=add_app).pack()
            tk.Button(top, text="Remove", command=remove_app).pack()

    def save_func(self):
        auto_exe = False
        auto_jpg = False
        auto_apk = False
        auto_torrent = False
        auto_zips = False
        auto_jars = False
        auto_pdfs = False
        auto_apps = False
        voice_commands = False

        if self.auto_exe_var.get() == 1:
            auto_exe = True
        if self.auto_jpg_var.get() == 1:
            auto_jpg = True
        if self.auto_apk_var.get() == 1:
            auto_apk = True
        if self.auto_torrent_var.get() == 1:
            auto_torrent = True
        if self.auto_zips_var.get() == 1:
            auto_zips = True
        if self.auto_jars_var.get() == 1:
            auto_jars = True
        if self.auto_pdfs_var.get() == 1:
            auto_pdfs = True
        if self.auto_apps_var.get() == 1:
            auto_apps = True
        if self.voice_commands_var.get() == 1:
            voice_commands = True

        with open("./settings.json", "r+") as e:
            settings = json.load(e)
            settings["auto_exe"] = auto_exe
            settings["auto_jpg"] = auto_jpg
            settings["auto_apk"] = auto_apk
            settings["auto_torrent"] = auto_torrent
            settings["auto_zips"] = auto_zips
            settings["auto_jars"] = auto_jars
            settings["auto_pdfs"] = auto_pdfs
            settings["auto_apps"] = auto_apps
            settings["voice_commands"] = voice_commands

            e.seek(0)
            json.dump(settings, e, indent=4)
            e.truncate()

        messagebox.showinfo(title="Automate", message="Saved")

        root.destroy()

        App.main()

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()