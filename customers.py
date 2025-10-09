import re

from PyQt6 import QtCore
from PyQt6.QtWidgets import QTableWidget, QWidget
from PyQt6.uic.Compiler.qtproxies import QtWidgets

import globals
from connection import *

class Customers:
    @staticmethod
    def checkDni(self=None):
        try:
            dni = globals.ui.txt_dnicif.text()
            dni = str(dni).upper()
            globals.ui.txt_dnicif.setText(dni)
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    globals.ui.txt_dnicif.setStyleSheet('background-color: rgb(255, 255, 220); color: black')
                else:
                    globals.ui.txt_dnicif.setStyleSheet('background-color:#FFC0CB; color: black')
                    globals.ui.txt_dnicif.setText(None)
                    globals.ui.txt_dnicif.setFocus()
            else:
                globals.ui.txt_dnicif.setStyleSheet('background-color:#FFC0CB; color: black')
                globals.ui.txt_dnicif.setText(None)
                globals.ui.txt_email.setPlaceholderText("Invalid DNI")
                globals.ui.txt_dnicif.setFocus()
        except Exception as error:
            print("error en validar dni ", error)

    @staticmethod
    def checkMail(self=None):
        email = globals.ui.txt_email.text()
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            globals.ui.txt_email.setStyleSheet('background-color: rgb(255, 255, 220); color: black')
        else:
            globals.ui.txt_email.setStyleSheet('background-color:#FFC0CB; color: black')
            globals.ui.txt_email.setText(None)
            globals.ui.txt_email.setPlaceholderText("Invalid email")
            globals.ui.txt_email.setFocus()

    @staticmethod
    def checkMobile(self=None):
        number = globals.ui.txt_phone.text()
        pattern = r'^[67]\d{8}$'
        if re.match(pattern, number):
            globals.ui.txt_phone.setStyleSheet('background-color: rgb(255, 255, 220); color: black')
        else:
            globals.ui.txt_phone.setStyleSheet('background-color:#FFC0CB; color: black')
            globals.ui.txt_phone.setText(None)
            globals.ui.txt_phone.setPlaceholderText("Invalid phone")
            globals.ui.txt_phone.setFocus()

    def loadTable(self):
        try:
            listTabCustomers = Connection.getCustomers()
            print(listTabCustomers)
            index = 0
            for record in listTabCustomers:
                globals.ui.tableWidget.setRowCount(index + 1)
                globals.ui.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(str(record[2])))
                globals.ui.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(str(record[3])))
                globals.ui.tableWidget.setItem(index, 2, QtWidgets.QTableWidgetItem(str(record[5])))
                globals.ui.tableWidget.setItem(index, 3, QtWidgets.QTableWidgetItem(str(record[7])))
                globals.ui.tableWidget.setItem(index, 4, QtWidgets.QTableWidgetItem(str(record[8])))
                globals.ui.tableWidget.setItem(index, 5, QtWidgets.QTableWidgetItem(str(record[9])))
                globals.ui.tableWidget.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                globals.ui.tableWidget.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignVCenter)
                globals.ui.tableWidget.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignCenter)
                globals.ui.tableWidget.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignCenter)
                globals.ui.tableWidget.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignCenter)
                globals.ui.tableWidget.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter.AlignCenter)
                index += 1
        except Exception as error:
            print("error en loadTable ", error)

    @staticmethod
    def selectCustomer():
        try:
            row_selected = globals.ui.tableWidget.selectedItems()
            mobile_customer_selected = row_selected[2].text()
            all_customer_data = Connection.getCustomerData(str(mobile_customer_selected))

            all_data_boxes = [globals.ui.txt_dnicif, globals.ui.txt_registrationdate, globals.ui.txt_surname, globals.ui.txt_name,
                              globals.ui.txt_email, globals.ui.txt_phone, globals.ui.txt_address]

            for i in range(len(all_data_boxes)):
                all_data_boxes[i].setText(all_customer_data[i])

            globals.ui.cmb_provinces.setCurrentText(str(all_customer_data[7]))
            globals.ui.cmb_cities.setCurrentText(str(all_customer_data[8]))

            if str(all_customer_data[9]) == "paper":
                globals.ui.rb_paper.setChecked(True)
            else:
                globals.ui.rb_electronic.setChecked(True)

            print("rowSelected: ", all_customer_data)
        except Exception as error:
            print("error en selectCustomer ", error)



    def capitalize(text, widget):
        try:
            capitalizedtext = str(text).title()
            widget.setText(capitalizedtext)

        except Exception as error:
            print("Error while capitalizing the name/surname ", error)