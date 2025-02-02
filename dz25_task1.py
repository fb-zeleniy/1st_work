# from tkinter import *
#
# window = Tk()
# window.title ("Всем салам")
#
#
# lbl1 = Label(window, text="дарова")
# lbl1.grid(column=0, row=0)
# window.geometry("400x500")
#
# def clicked():
#     lbl1.configure(text="Я же говорил не нажимай")
# btn1 = Button(window, text="Не жмай", command=clicked)
# btn1.grid(column=0, row=0)
# window.mainloop()

import tkinter as tk
from tkinter import messagebox
import requests


def fetch_data():
    post_id = entry.get()
    if not post_id.isdigit():
        messagebox.showerror("Ошибка", "id должен быть числом")
        return

    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Заголовок: {data['title']}\n\n{data['body']}")
    else:
        messagebox.showerror("Ошибка", "не удалось получить данные")



root = tk.Tk()
root.title("Jsob place holder")
root.size("400x300")


label1 = tk.Label(root, text="Введите id поста:")
label1.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

button1 = tk.Button(root, text="Получить данные", command=fetch_data)
button1.pack(pady=5)

output_text = tk.Text(root, height=10, width=50)
output_text.pack(pady=5)

if __name__ == 'main':
 root.mainloop()
