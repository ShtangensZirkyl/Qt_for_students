import sys
import pandas as pd

from PyQt5 import QtWidgets

from models.PandasModel import PandasModel
from ui.MainWindow import Ui_MainWindow


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self.__import_data()

    def __import_data(self):
        data = pd.read_excel('./data/1.xlsx')
        model = PandasModel(data)
        self._ui.tableView.setModel(model)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = App()
    main_window.show()
    app.exec()
