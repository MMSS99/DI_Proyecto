import events
import globals
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