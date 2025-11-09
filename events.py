import sys

import connection
import globals
import time
import datetime
import zipfile
import os
import csv
from PyQt6 import QtWidgets, QtCore, QtGui
from customers import *
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
            list = Connection.listProv()
            globals.ui.cmb_provinces.addItems(list)
        except Exception as e:
            print("Failed to load data into province list", e)

    def loadMuni(self=None):
        try:
            province = globals.ui.cmb_provinces.currentText()
            list = Connection.listMuniProv(province)
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


    @staticmethod
    def saveBackup():
        try:
            date = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            filename = str(date + '_backup.zip')
            file_path, _ = globals.dialog_open.getSaveFileName(None, "Save Backup file", filename, 'zip')

            if globals.dialog_open.accept and file_path:
                with zipfile.ZipFile(file_path, 'w', zipfile.ZIP_DEFLATED) as filezip:
                    filezip.write('./data/bbdd.sqlite', os.path.basename('bbdd.sqlite'))

                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon("img/gabrielgsd.jpg"))
                mbox.setWindowTitle('Save Backup')
                mbox.setText('Done saving backup')
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.exec()
                return

            mbox = QtWidgets.QMessageBox()
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            mbox.setText("An error has ocurred while saving the backup")
            mbox.setWindowTitle('Error')
            mbox.exec()

        except Exception as e:
            print("Error en saveBackup: ", e)
    @staticmethod
    def restoreBackup():
        try:
            filename = globals.dialog_open.getOpenFileName(None, "Restore Backup file", '', '*.zip;;All Files (*)')
            file = filename[0]
            if file:
                with zipfile.ZipFile(file, 'r', zipfile.ZIP_DEFLATED) as bbdd:
                    bbdd.extractall(pwd='./data')

                bbdd.close()

                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon("img/gabrielgsd.jpg"))
                mbox.setWindowTitle('Successfully')
                mbox.setText('Successfully restored backup')
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.exec()

                connection.Connection.db_connection()
                Events.loadProv()
                Events.loadMuni()
                Customers.loadTable()

        except Exception as e:
            print("Error en restoreBackup: ", e)

    @staticmethod
    def exportCustomersToCsv():
        try:
            date = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            filename = str(date + '_customers.csv')
            file_path, _ = globals.dialog_open.getSaveFileName(None, "Export customers data", filename, 'CSV Files (*.csv)')

            if file_path:
                all_customers_data = Connection.getCustomers()
                with open(file_path, 'w', newline='', encoding='utf-8') as csvFile:
                    writer = csv.writer(csvFile)

                    header_rows = [
                        "dni_nie",
                        "adddata",
                        "surname",
                        "name",
                        "mail",
                        "mobile",
                        "address",
                        "province",
                        "city",
                        "invoicetype",
                        "historical"
                    ]

                    writer.writerow(header_rows)
                    writer.writerows(all_customers_data)



                mbox = QtWidgets.QMessageBox()
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setWindowIcon(QtGui.QIcon("img/gabrielgsd.jpg"))
                mbox.setWindowTitle('Exported customers')
                mbox.setText('Successfully exported customers data')
                mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                mbox.exec()
                return

            mbox = QtWidgets.QMessageBox()
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            mbox.setWindowTitle('Error')
            mbox.setText("An error has ocurred while exporting the customers data")
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
            mbox.exec()


        except Exception as e:
            print("Error en exportCustomersToXsl: ", e)
            mbox = QtWidgets.QMessageBox()
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            mbox.setWindowTitle('Exception')
            mbox.setText("An unexpected error has occurred")
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
            mbox.exec()

    @staticmethod
    def showStatusBar():
        try:
            today = datetime.datetime.now().strftime("%d/%m/%Y")
            label_status = QtWidgets.QLabel()
            label_status.setText("Date: " + today + " - " + "Versión 0.0.1")
            label_status.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            globals.ui.statusbar.addPermanentWidget(label_status, 1)
        except Exception as e:
            print("Error en showStatusBar: ", e)
