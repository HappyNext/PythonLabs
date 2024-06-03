import sys
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        colors = ['#053061', '#2166ac', '#4393c3', '#92c5de', '#d1e5f0', '#f7f7f7', '#fddbc7',
                  '#f4a582', '#d6604d', '#b2182b', '#67001f']
        if role == Qt.BackgroundRole:
            value = self._data[index.row()][index.column()]
            if (isinstance(value, int) or isinstance(value, float)):
                value = int(value)  # Convert to integer for indexing.
                # Limit to range -5 ... +5, then convert to 0..10
                value = max(-5, value)  # values < -5 become -5
                value = min(5, value)  # valaues > +5 become +5
                value = value + 5  # -5 becomes 0, +5 becomes + 10
                return QtGui.QColor(colors[value])
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
            [1, 0, 0],
            [3, 5, 0],
            [3, 3, 2],
            [7, 8, 9],
        ]
        self.model = TableModel(data)
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()