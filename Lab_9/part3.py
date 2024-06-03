from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QLabel, QAction
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("part3.ui", self)
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.setCentralWidget(self.label)
        self.load = self.findChild(QAction, 'action')
        self.load.triggered.connect(self.load_picture)
        self.clear = self.findChild(QAction, 'action_2')
        self.clear.triggered.connect(self.clear_picture)

    def load_picture(self):
        options = QFileDialog.Options()
        picture, _ = QFileDialog.getOpenFileName(self, "Open image", "",
                                                 "Images (*.png *.xpm *.jpg *.bmp *.gif);;All Files (*)",
                                                 options=options)
        if picture:
            self.label.setPixmap(QPixmap(picture))
        else:
            print("No picture selected")
    def clear_picture(self):
        self.label.setPixmap(QPixmap())


# Create the application instance
app = QApplication(sys.argv)

# Create and display the main window
w = MainWindow()
w.show()

# Start the main application loop
sys.exit(app.exec_())
