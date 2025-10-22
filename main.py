from PyQt6.QtWidgets import QTableWidget, QWidget

import events
import globals
from venAux import *
from customers import *
from events import *
from window import *
from connection import *
import sys

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        globals.ui = Ui_main_window()
        globals.ui.setupUi(self)

        #instancias
        globals.dlg_calendar = Calendar()
        globals.dlg_about = About()

        #conection
        Connection.db_connection()
        Customers.loadTable(self)
        Events.resizeTabCustomer(self)

        #functions in menu bar
        globals.ui.actionExit.triggered.connect(Events.messageExit)
        globals.ui.actionAbout.triggered.connect(Events.showAbout)

        #functions in entries
        globals.ui.txt_dnicif.editingFinished.connect(Customers.checkDni)
        globals.ui.txt_name.editingFinished.connect(lambda: Customers.capitalize(globals.ui.txt_name.text(), globals.ui.txt_name))
        globals.ui.txt_surname.editingFinished.connect(lambda: Customers.capitalize(globals.ui.txt_surname.text(), globals.ui.txt_surname))
        globals.ui.txt_email.editingFinished.connect(Customers.checkMail)
        globals.ui.txt_phone.editingFinished.connect(Customers.checkMobile)

        #funcitons in table
        globals.ui.tableWidget.clicked.connect(Customers.selectCustomer)

        #functions in buttons
        globals.ui.btn_calendar.clicked.connect(Events.openCalendar)
        globals.ui.btn_clean.clicked.connect(Events.clearEntries)
        globals.ui.btn_delete.clicked.connect(Customers.deleteCustomer)
        globals.ui.btn_save.clicked.connect(Customers.saveCustomer)
        globals.ui.btn_search.clicked.connect(Customers.searchCustomer)
        globals.ui.btn_modify.clicked.connect(Customers.modifyCustomer)

        #functions in combobox
        Events.loadProv(self)
        globals.ui.cmb_provinces.currentIndexChanged.connect(events.Events.loadMuni)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.setWindowIcon(QtGui.QIcon("./img/logo.ico"))
    window.showMaximized()
    sys.exit(app.exec())

#16 octubre exámen teórico
#14 noviembre exámen práctico
