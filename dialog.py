from PyQt5 import QtWidgets


class Dialog(QtWidgets.QDialog):
    def __init__(self, params_signal):
        super().__init__()
        self.dialog_layout = QtWidgets.QVBoxLayout(self)
        self.btn = QtWidgets.QPushButton('ok')
        self.dialog_layout.addWidget(self.btn)
        self.setLayout(self.dialog_layout)
        self.params_signal = params_signal
        self.__add_callbacks()

    def __add_callbacks(self):
        self.btn.clicked.connect(self.__end_dialog)

    def __end_dialog(self):
        self.params_signal.emit('Hello')
        self.accept()
