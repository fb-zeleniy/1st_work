import sys
from PyQt6.QtWidgets import  QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
import requests
class NewApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Js place holder")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.label = QLabel("Введите id поста:")
        layout.addWidget(self.label)

        self.entry = QLineEdit()
        layout.addWidget(self.entry)

        self.button = QPushButton("гет  данные")
        self.button.clicked.connect(self.fetch_data)
        layout.addWidget(self.button)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        self.setLayout(layout)

     def fetch_data(self):
        post_id = self.entry.text()
        if not post_id.isdigit():

           QMessageBox.critical("Ошибка")
           QMessageBox.critical(self, "Подсказка", "ID должен быть числом.")
           return

        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.output_text.setPlainText(f"Заголовок: {data['title']}\n\n{data['body']}")
        else:
            QMessageBox.critical(self, "Ошибка, не удалось получить данные")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewApp()
    window.show()
    sys.exit(app.exec())
