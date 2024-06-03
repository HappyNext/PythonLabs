import random
from PyQt5.QtWidgets import ( QMainWindow, QApplication, QLabel, QWidget, QVBoxLayout, QPushButton)
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        layout = QVBoxLayout()

        self.label = QLabel("Семененко Олег Сергійович")
        self.label.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)

        layout.addWidget(self.label)

        self.button = QPushButton("Change Color")
        self.button.clicked.connect(self.change_color)

        layout.addWidget(self.button)

        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

        self.resize(800, 600)

    def change_color(self):
        new_color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.label.setStyleSheet("color: %s;" % new_color.name())

app = QApplication([])
w = MainWindow()
w.show()
app.exec()