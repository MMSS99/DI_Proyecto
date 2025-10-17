import sys

import connection
import globals
import time
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QTableWidget, QWidget

class Events:
    @staticmethod
    def messageExit(self=None):
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
            mbox.setWindowIcon(QtGui.QIcon("./img/logo.ico"))
            mbox.setWindowTitle("Exit")
            mbox.setText("Are you sure you want to exit?")
            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
            mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText("Yes")
            mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText("Go back")
            mbox.resize(600, 800)

            if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
                sys.exit()
            else:
                mbox.hide()

        except Exception as e:
            print("Error while exiting", e)

    def openCalendar(self=None):
        try:
            globals.dlg_calendar.show()


        except Exception as e:
            print("Error while opening the calendar window", e)

    def clearEntries(self=None):
        try:
            for text in [globals.ui.txt_dnicif,
                            globals.ui.txt_registrationdate,
                            globals.ui.txt_surname,
                            globals.ui.txt_name,
                            globals.ui.txt_email,
                            globals.ui.txt_phone,
                            globals.ui.txt_address]:
                text.clear()

            for combo in [globals.ui.cmb_cities, globals.ui.cmb_cities]:
                combo.setCurrentIndex(-1)

            globals.ui.rbt_digitalbill.setChecked(True)
            globals.ui.chk_inactive.setChecked(False)

        except Exception as error:
            print("!!! (Events.clearEntries) Error clearing entries", error)

    def showAbout(self=None):
        try:
            globals.dlg_about.show()
        except Exception as e:
            print("Error while showing the about window", e)


    def loadData(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            if globals.ui.tabWidget_main.currentIndex() == 0:
                globals.ui.txt_registrationdate.setText(data)
            time.sleep(0.3)
            globals.dlg_calendar.hide()

        except Exception as e:
            print("Failed to load data into registration date", e)

    def loadProv(self=None):
        try:
            globals.ui.cmb_provinces.clear()
            list = connection.Connection.listProv(self)
            globals.ui.cmb_provinces.addItems(list)
        except Exception as e:
            print("Failed to load data into province list", e)

    def loadMuni(self=None):
        try:
            province = globals.ui.cmb_provinces.currentText()
            list = connection.Connection.listMuniProv(province)
            globals.ui.cmb_cities.clear()
            globals.ui.cmb_cities.addItems(list)
        except Exception as e:
            print("Failed to load data into municipalities list", e)

    def resizeTabCustomer(self):
        try:
            header = globals.ui.tableWidget.horizontalHeader()
            for i in range(header.count()):
                if i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                else:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                header_items = globals.ui.tableWidget.horizontalHeaderItem(i)
                font = header_items.font()
                font.setBold(True)
                header_items.setFont(font)

        except Exception as e:
            print("Failed to resize tab header", e)
