import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMdiArea, QMdiSubWindow, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Настройка главного окна
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 800, 600)

        # Создание MDI области (Multiple Document Interface)
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        # Создание меню
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("File")

        # Добавление действия в меню для создания нового окна
        newWindowAction = QAction("New Window", self)
        newWindowAction.triggered.connect(self.create_new_window)
        fileMenu.addAction(newWindowAction)

        # Добавление действия для каскадного расположения окон
        cascadeAction = QAction("Cascade", self)
        cascadeAction.triggered.connect(self.cascade_windows)
        fileMenu.addAction(cascadeAction)

    def create_new_window(self):
        # Создание нового подокна
        sub = QMdiSubWindow()
        sub.setWidget(QTextEdit())
        sub.setWindowTitle("Sub Window")
        self.mdi.addSubWindow(sub)
        sub.show()

    def cascade_windows(self):
        # Каскадное расположение подокон
        self.mdi.cascadeSubWindows()

# Создаем экземпляр приложения
app = QApplication(sys.argv)

# Создаем главное окно
main_window = MainWindow()
main_window.show()

# Запуск главного цикла приложения
sys.exit(app.exec_())

