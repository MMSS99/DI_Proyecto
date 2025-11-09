import events
import globals
from dlg_about import Ui_dlg_about
from dlg_calendar import *
from datetime import datetime

class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        globals.dlg_calendar = Ui_dlg_calendar()
        globals.dlg_calendar.setupUi(self)
        day = datetime.now().day
        month = datetime.now().month
        year = datetime.now().year

        globals.dlg_calendar.calendarWidget.setSelectedDate((QtCore.QDate(year, month, day)))
        globals.dlg_calendar.calendarWidget.clicked.connect(events.Events.loadData)

class About(QtWidgets.QDialog):
    def __init__(self):
        super(About, self).__init__()
        globals.dlg_about = Ui_dlg_about()
        globals.dlg_about.setupUi(self)

        globals.dlg_about.btn_closeAbout.clicked.connect(lambda: globals.dlg_about.hide())

class FileDialog(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialog, self).__init__()
