from PyQt6.QtWidgets import QTableWidget, QWidget

import globals
from customers import *
from events import *
from window import *
import sys

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        globals.ui = Ui_main_window()
        globals.ui.setupUi(self)
        #functions in menu bar
        globals.ui.actionExit.triggered.connect(Events.messageExit)

        #functions in entries
        globals.ui.txt_dnicif.editingFinished.connect(Customers.checkDni)

        #functions in buttons
        globals.ui.btn_calendar.clicked.connect(Events.openCalendar)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.setWindowIcon(QtGui.QIcon("./img/logo.ico"))
    window.showMaximized()
    sys.exit(app.exec())