from PyQt5 import QtCore, Qt
import pandas as pd
from PyQt5.QtCore import QModelIndex


class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, data: pd.DataFrame):
        super().__init__()
        self.__data = data

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.__data.values)

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return self.__data.columns.size

    def data(self, index: QModelIndex, role: int = ...):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self.__data.values[index.row()][index.column()])
        else:
            return None

    def headerData(self, section: int, orientation, role: int = ...):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return str(self.__data.columns[section])
        else:
            return None

    def setData(self, index: QModelIndex, value, role: int = ...) -> bool:
        if not index.isValid():
            return False
        if role != QtCore.Qt.EditRole:
            return False
        row = index.row()
        if (row < 0) and (row >= len(self.__data.values)):
            return False
        column = index.column()
        if (column < 0) and (column >= self.__data.columns.size):
            return False
        self.__data.values[row][column] = value
        self.dataChanged.emit(index, index)
        return True

    def flags(self, index: QModelIndex):
        flags = QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
        return flags
