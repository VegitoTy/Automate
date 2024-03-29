import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import json
import App

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

            self.auto_exe_var = tk.IntVar(value=auto_exe)
            self.auto_jpg_var = tk.IntVar(value=auto_jpg)
            self.auto_apk_var = tk.IntVar(value=auto_apk)
            self.auto_torrent_var = tk.IntVar(value=auto_torrent)
            self.auto_zips_var = tk.IntVar(value=auto_zips)
            self.auto_jars_var = tk.IntVar(value=auto_jars)
            self.auto_pdfs_var = tk.IntVar(value=auto_pdfs)
            self.auto_apps_var = tk.IntVar(value=auto_apps)

        ft = tkFont.Font(family='Times', size=18)

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

        self.save = tk.Button(root, text="Save", font=ft, justify="center", command=self.save_func)
        self.save.pack()

    def save_func(self):
        auto_exe = False
        auto_jpg = False
        auto_apk = False
        auto_torrent = False
        auto_zips = False
        auto_jars = False
        auto_pdfs = False
        auto_apps = False

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
# epitome of repetitivness
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