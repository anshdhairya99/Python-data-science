import tkinter as tk
from tkinter import ttk, filedialog
import requests
import os
# Refrence link :-----

# https://r3---sn-ci5gup-8onl.gvt1.com/edgedl/android/studio/install/2022.3.1.18/android-studio-2022.3.1.18-windows.exe?cms_redirect=yes&mh=qK&mip=2401:4900:8026:3fbf:d84c:7d3:8bc9:5233&mm=28&mn=sn-ci5gup-8onl&ms=nvh&mt=1691953467&mv=m&mvi=3&pcm2cms=yes&pl=44&shardbypass=sd
# https://download.sublimetext.com/sublime_text_build_4152_x64_setup.exe
# https://download-cdn.jetbrains.com/python/pycharm-professional-2023.2.exe

class Downloader:
    def __init__(self):
        self.saveto = ""
        self.window = tk.Tk()
        self.window.title("Python GUI Downloader")
        self.url_label = tk.Label(text="Enter the URL")
        self.url_label.pack()
        self.url_entry = tk.Entry()
        self.url_entry.pack()
        self.browse_button = tk.Button(text="Browse",command=self.browse_file)
        self.browse_button.pack()
        self.download_button = tk.Button(text="Download",command=self.download)
        self.download_button.pack()
        self.window.geometry("844x344")
        self.progress_bar = ttk.Progressbar(self.window, orient="horizontal", maximum=100, length=200, mode="determinate")
        self.progress_bar.pack()
        self.window.mainloop()

    def browse_file(self):
        saveto=filedialog.asksaveasfilename(initialfile=self.url_entry.get().split("/")[-1].split("?")[0])
        self.saveto = saveto

    def download(self):
        url = self.url_entry.get()
        response = requests.get(url, stream=True)
        total_size_in_bytes = 100
        if(response.headers.get("content_length")):
           total_size_in_bytes = int(response.headers.get("content-length"))
        block_size = 10000
        self.progress_bar["value"] = 0
        fileName = self.url_entry.get().split("/")[-1].split("?")[0]
        if(self.saveto == ""):
            self.saveto = fileName

        print(self.saveto)
        with open(self.saveto, "wb") as f:
            for data in response.iter_content(block_size):
                self.progress_bar["value"] += (100*block_size)/total_size_in_bytes
                self.window.update()
                f.write(data)

Downloader()
