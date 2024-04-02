import sys
import pandas as pd

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSortFilterProxyModel

from models.PandasModel import PandasModel, SortFilterProxyModel
from ui.MainWindow import Ui_MainWindow
from ui.dialog import Dialog


class App(QtWidgets.QMainWindow):
    dialog_params = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self._data = pd.read_excel('./data/1.xlsx')
        self.__set_table()
        self.__add_callbacks()

    def __set_table(self):
        model = PandasModel(self._data)
        proxy_model = SortFilterProxyModel()
        proxy_model.setSourceModel(model)
        self._ui.tableView.setModel(proxy_model)
        self._ui.tableView.setSortingEnabled(True)

    def __add_callbacks(self):
        self._ui.filter_button.clicked.connect(self.__open_filter_dialog)
        self.dialog_params.connect(self.__get_params_from_dialog)

    def __get_params_from_dialog(self, value):
        print(value)

    def __open_filter_dialog(self):
        self.dialog = Dialog(self.dialog_params)

        self.dialog.show()
    # def __import_data(self):
        # data = pd.read_excel('./data/1.xlsx')
        # model = PandasModel(data)
        # self._ui.tableView.setModel(model)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = App()
    main_window.show()
    app.exec()
