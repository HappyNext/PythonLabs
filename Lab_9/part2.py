from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QSpinBox, QVBoxLayout, QWidget, QMessageBox
from PyQt5.uic import loadUi
import csv

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            loadUi("part2.ui", self)  # Загрузка дизайна из файла .ui
        except Exception as e:
            print(f"Ошибка при загрузке UI: {e}")
            return

        self.save_button.clicked.connect(self.save_data)

    def save_data(self):
        student = self.student_line.text()
        discipline = self.discipline_line.text()
        mark = self.mark_spin.value()

        if student and discipline:
            try:
                with open("data.csv", "a", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([student, discipline, mark])
                QMessageBox.information(self, "Успех", "Данные успешно сохранены!")
            except Exception as e:
                QMessageBox.warning(self, "Ошибка", f"Ошибка при сохранении данных: {e}")
        else:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля.")

# Создание экземпляра приложения
app = QApplication([])

# Создание и отображение главного окна
w = MainWindow()
w.show()

# Запуск главного цикла приложения
app.exec_()
