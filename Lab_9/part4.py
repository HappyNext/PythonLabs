import sys
import csv
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QRadioButton, QProgressBar, QPushButton, QLabel, QButtonGroup, QMessageBox)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student Grades")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        # Create radio buttons
        self.radio_student = QRadioButton("Студент")
        self.radio_subject = QRadioButton("Дисциплина")
        self.radio_grade = QRadioButton("Оценка")

        self.radio_grade.setChecked(True)  # Set default checked button

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radio_student)
        self.button_group.addButton(self.radio_subject)
        self.button_group.addButton(self.radio_grade)

        self.layout.addWidget(self.radio_student)
        self.layout.addWidget(self.radio_subject)
        self.layout.addWidget(self.radio_grade)

        # Create progress bar
        self.progress_bar = QProgressBar()
        self.layout.addWidget(self.progress_bar)

        # Create label to show selected data
        self.data_label = QLabel("Выбранные данные")
        self.layout.addWidget(self.data_label)

        # Create button to load data
        self.load_button = QPushButton("Загрузить данные")
        self.load_button.clicked.connect(self.load_data)
        self.layout.addWidget(self.load_button)

        self.central_widget.setLayout(self.layout)

    def load_data(self):
        # Read data from CSV file
        file_path = 'data.csv'  # путь к вашему CSV файлу
        data = []

        # Попытка открытия файла в разных кодировках
        encodings = ['utf-8', 'cp1251', 'latin1']
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    reader = csv.reader(file)
                    next(reader)  # Пропускаем заголовок
                    for row in reader:
                        if len(row) != 3:
                            print(f"Invalid row format: {row}")  # Вывод отладочной информации
                            raise ValueError(f"Invalid row format: {row}")
                        data.append(row)
                break  # Если удалось прочитать файл, выходим из цикла
            except Exception as e:
                last_exception = e

        if not data:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные: {last_exception}")
            return

        selected_radio = self.button_group.checkedButton()

        if selected_radio == self.radio_student:
            # Show student data
            student_data = [row[0] for row in data]
            self.data_label.setText("Студенты: " + ", ".join(student_data))

        elif selected_radio == self.radio_subject:
            # Show subject data
            subject_data = [row[1] for row in data]
            self.data_label.setText("Дисциплины: " + ", ".join(subject_data))

        elif selected_radio == self.radio_grade:
            # Show grades in progress bar
            grades = []
            for row in data:
                try:
                    grades.append(int(row[2]))
                except ValueError:
                    print(f"Invalid grade value: {row[2]}")  # Вывод отладочной информации
                    QMessageBox.warning(self, "Ошибка", f"Некорректное значение оценки: {row[2]}")
            if grades:
                average_grade = int(sum(grades) / len(grades)) * 20 # Convert to % for QProgressBar
                self.progress_bar.setValue(average_grade)
                self.data_label.setText("Средняя оценка: {:.2f}".format(sum(grades) / len(grades)))
            else:
                self.progress_bar.setValue(0)
                self.data_label.setText("Нет данных для отображения")

# Создание экземпляра приложения
app = QApplication([])

# Создание и отображение главного окна
w = MainWindow()
w.show()

# Запуск главного цикла приложения
app.exec_()
