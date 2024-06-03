import sys
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ForegroundRole:
            value = self._data[index.row()][index.column()]
            if ((isinstance(value, int) or isinstance(value, float))
                    and value < 0):
                return QtGui.QColor('red')
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
        [4, 9, 2],
        [1, -1, 'hello'],
        [3.023, 5, -5],
        [3, 3, datetime(2017,10,1)],
        [7.555, 8, 9],
        ]
        self.model = TableModel(data)
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()