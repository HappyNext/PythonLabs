import sys
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DecorationRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime):
                return QtGui.QIcon('calendar.jpg')
            if isinstance(value, bool):
                if value:
                    return QtGui.QIcon('tick.jpg')
                return QtGui.QIcon('cross.png')
        if role == Qt.DisplayRole:
            # Отримання значення
            value = self._data[index.row()][index.column()]
            # Перевірка кожного типу та візуалізація відповідно
            if isinstance(value, datetime):
                # Відобразити час до РРРР-ММ-ДД.
                return value.strftime("%Y-%m-%d")
            if isinstance(value, float):
                # Візуалізувати плаваюче значення до 2 знаків
                return "%.2f" % value
            if isinstance(value, str):
                # Виводити рядки в лапки
                return '"%s"' % value
            # За замовчуванням (наприклад, int)
            return value

    def rowCount(self, index):
    # Довжина зовнішнього списку.
        return len(self._data)
    def columnCount(self, index):
    # Беремо перший підсписок і повертаємо довжину
    # (працює, лише якщо всі рядки мають однакову довжину) 4
        return len(self._data[0])
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.table = QtWidgets.QTableView()
        data = [
            [bool(True), 9, 2],
            [1, 0, -1],
            [3, 5, bool(False)],
            [3, 3, 2],
            [datetime(2019,5,4), 8, 9],
        ]
        self.model = TableModel(data)
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()