from PyQt6.QtWidgets import QTableWidget, QWidget

from events import *
from window import *
import sys

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        #functions in menu bar
        self.ui.actionExit.triggered.connect(Events.messageExit)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.setWindowIcon(QtGui.QIcon("./img/logo.ico"))
    window.showMaximized()
    sys.exit(app.exec())