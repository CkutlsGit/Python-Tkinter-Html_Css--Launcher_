import tkinter as tk
from tkinter.font import Font
from tkinter import *
import os
import urllib.request

root = tk.Tk()
root.geometry("400x400")
root.title("Setup Launcher")

def downoald():
    url = "https://drive.google.com/file/d/1Gl_qGtIdVerp_8VzsXZZlnHjgNKO8APb/view?usp=share_link"
    filename = "launcher.py"
    path = "C:/Downloads"
    filepath = os.path.join(path, filename)
    if not os.path.exists(path):
        os.makedirs(path)
    urllib.request.urlretrieve(url, filepath)
    print("Скачено!")
    
btn_setup = tk.Button(text="Начать скачивание", command=downoald)
btn_setup.place(relx = 0.5 , rely = 0.4, anchor = CENTER)

root.mainloop()