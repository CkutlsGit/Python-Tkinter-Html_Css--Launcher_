import tkinter as tk
from tkinter.font import Font
from tkinter import *
import os
import urllib.request
import zipfile

#Функция для создания папки в которой будет игра

#Функция для скачивания файлов
def downoald():
    url = "https://drive.google.com/drive/folders/1hgktEbEGNLZRESF88Dy2qQDc_hPp3I4E?usp=share_link"

    #Заранее созданая папка
    save_path = "D:/aboba"
    file_name = "game.zip"
    #Добавление файла в папку
    file_path = os.path.join(save_path, file_name)

    urllib.request.urlretrieve(url, file_path) #<--- Скачивание по url адресу и расархирировать zip file
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(save_path)

root = tk.Tk()
root.geometry("600x600") #<--- Настройки для окна
root.configure(bg="#BADBAD")


text = tk.Label(root, text="Нажми на кнопку для запуска игры!", font=("Arial", 24), bg="#BADBAD") #<--- Настройка и расположение текста
text.place(relx = 0.5 , rely = 0.4, anchor = CENTER)

btn = tk.Button(root, text="Запуск игры!", font=("Arial", 16), bg="#4CC332", command=downoald) #<---- Настройка и расположение кнопки
btn.place(relx = 0.5 , rely = 0.6, anchor = CENTER )

root.mainloop()