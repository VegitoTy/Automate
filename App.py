# Automate
# epicness by VegitoTy

from funcs import auto_exe, auto_jpg, auto_torrents, auto_apk, auto_zips, auto_pdfs, auto_apps
import time
import os
import json
import multiprocessing
import psutil

def get_downloads():
    with open("./data.json", "r+") as e:
        data = json.load(e)
        executables = data["Executables"]
    download_list = []
    for file in os.listdir("C:/Users/pc/Downloads"):
        file = f"C:/Users/pc/Downloads/{file}"
        if os.path.isfile(file):
            file_exists = False
            for item in executables:
                if os.path.splitext(file) == os.path.splitext(item): file_exists = True
            if not file_exists: download_list.append(file)
    return download_list

def get_extension(file):
    name, extension = os.path.splitext(file)
    return extension 

def ask_auto_apps(): # soooooooooon
    pass

def main():

    convert_jpg = [".avif", ".webp", ".png", ".jpeg", ".tiff", ".raw", ".heif", ".jpg"]
    zips = [".7z", ".zip", ".rar"]
    convert_pdf = [".pptx", ".pdf", ".ppt"]

    with open("./settings.json", "r+") as e:
        settings = json.load(e)

        if not os.path.exists("C:/Users/pc/Downloads/Images"): # bad
            os.mkdir("C:/Users/pc/Downloads/Images")
        if not os.path.exists("C:/Users/pc/Downloads/Torrents"):
            os.mkdir("C:/Users/pc/Downloads/Torrents")
        if not os.path.exists("C:/Users/pc/Downloads/APKs"):
            os.mkdir("C:/Users/pc/Downloads/APKs")
        if not os.path.exists("C:/Users/pc/Downloads/Compressed"):
            os.mkdir("C:/Users/pc/Downloads/Compressed")
        if not os.path.exists("C:/Users/pc/Downloads/PDFs"):
            os.mkdir("C:/Users/pc/Downloads/PDFs")

        auto_apps_process = multiprocessing.Process()

        if settings["auto_apps"]:
            auto_apps_process = multiprocessing.Process(target=auto_apps.AutoApps().main, daemon=True)
        auto_apps_process.start()

        while True:
            time.sleep(.3)

            while not auto_apps_process.is_alive():
                time.sleep(10)
                if psutil.cpu_percent() < 70 and psutil.virtual_memory().percent < 70:
                    auto_apps_process = multiprocessing.Process(target=auto_apps.AutoApps().main, daemon=True)
                    auto_apps_process.start()

            download_list = get_downloads()
            for file in download_list:
                extension = get_extension(file)
                if extension == ".exe" and settings["auto_exe"]:
                    auto_exe.exe_algorithm(file)
                elif extension in convert_jpg and settings["auto_jpg"]:
                    auto_jpg.convert_jpg(file)
                elif extension == ".torrent" and settings["auto_torrent"]:
                    auto_torrents.torrent_algorithm(file)
                elif extension == ".apk" and settings["auto_apk"]:
                    auto_apk.apk_algorithm(file)
                elif extension in zips and settings["auto_zips"]:
                    auto_zips.zip_algorithm(file)
                elif extension == ".jars" and settings["auto_jars"]:
                    auto_zips.zip_algorithm(file)
                elif extension in convert_pdf and settings["auto_pdfs"]:
                    auto_pdfs.pdf_algorithm(file)

if __name__ == "__main__":
    main()