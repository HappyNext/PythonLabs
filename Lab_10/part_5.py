# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import datetime

# Цветовая палитра
COLORS = [
    '#e0f3db', '#ccebc5', '#a8ddb5', '#7bccc4',
    '#4eb3d3', '#2b8cbe', '#0868ac', '#084081',
    '#005824', '#00441b', '#002b12'
]


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime.datetime):
                return value.strftime("%Y-%m-%d")
            if isinstance(value, float):
                return "%.2f" % value
            if isinstance(value, str):
                return '"%s"' % value
            return value

        if role == Qt.DecorationRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, bool):
                if value:
                    return QtGui.QIcon('tick.png')
                return QtGui.QIcon('cross.png')
            if isinstance(value, datetime.datetime):
                return QtGui.QIcon('calendar.png')
            if (isinstance(value, int) or isinstance(value, float)):
                value = int(value)

                value = max(-5, value)
                value = min(5, value)
                value = value + 5
                return QtGui.QColor(COLORS[value])

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Window')
        self.setGeometry(400, 400, 600, 300)
        self.table = QtWidgets.QTableView()

        data = [
            [True, 9, 2],
            [1, 0, -1],
            [3, 5, False],
            [3, 3, 2],
            [datetime.datetime(2019, 5, 4), 8, 9],
        ]

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
