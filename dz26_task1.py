import tkinter as tk
from tkinter import messagebox
import requests


class New_App:
    def __init__(self, root):
        self.root = root
        self.root.title("JSONPlaceholder ")
        self.root.geometry("800x800")

        self.label = tk.Label(root, text="Введите ID поста:")
        self.label.pack(pady=5)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Получить данные", command=self.fetch_data)
        self.button.pack(pady=5)

        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.pack(pady=5)

    def fetch_data(self):
        post_id = self.entry.get()
        if not post_id.isdigit():
            messagebox.showerror("Ошибка")
            messagebox.showwarning("Подсказка", "ID должен быть числом.")

            return

        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"Заголовок: {data['title']}\n\n{data['body']}")
        else:
            messagebox.showerror("не удалось получить данные")


if __name__ == "__main__":
    root = tk.Tk()
    app = New_App(root)
    root.mainloop()
