from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        # Создаем кнопку
        self.button = QPushButton("Показать сообщение", self)
        self.button.setGeometry(50, 50, 200, 50)
        self.button.clicked.connect(self.show_message)

    def show_message(self):
        # Создаем диалоговое окно QMessageBox
        msg = QMessageBox()
        msg.setWindowTitle("Информационное сообщение")
        msg.setText("Это информационное сообщение.")

        # Добавляем стандартные кнопки в диалоговое окно
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)

        # Показываем диалоговое окно и ждем ответа пользователя
        result = msg.exec_()

        # Обрабатываем результат нажатия кнопки
        if result == QMessageBox.Ok:
            print("Нажата кнопка 'Ok'")
        elif result == QMessageBox.Cancel:
            print("Нажата кнопка 'Cancel'")
        elif result == QMessageBox.Ignore:
            print("Нажата кнопка 'Ignore'")


# Создание экземпляра приложения
app = QApplication(sys.argv)

# Создание и отображение главного окна
w = MainWindow()
w.show()

# Запуск главного цикла приложения
sys.exit(app.exec_())
