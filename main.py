from PyQt6.QtWidgets import QTableWidget, QWidget

import globals
from venAux import *
from customers import *
from events import *
from window import *
import sys

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        globals.ui = Ui_main_window()
        globals.ui.setupUi(self)
        #instancias
        globals.dlg_calendar = Calendar()

        #functions in menu bar
        globals.ui.actionExit.triggered.connect(Events.messageExit)

        #functions in entries
        globals.ui.txt_dnicif.editingFinished.connect(Customers.checkDni)
        globals.ui.txt_name.editingFinished.connect(Customers.capitalize)
        globals.ui.txt_surname.editingFinished.connect(Customers.capitalize)

        #functions in buttons
        globals.ui.btn_calendar.clicked.connect(Events.openCalendar)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.setWindowIcon(QtGui.QIcon("./img/logo.ico"))
    window.showMaximized()
    sys.exit(app.exec())