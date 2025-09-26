import re

import globals

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
        number = globals.ui.txt_mobile.text()
        pattern = r'^[67]\d{8}$'
        if re.match(pattern, number):
            globals.ui.txt_mobile.setStyleSheet('background-color: rgb(255, 255, 220); color: black')
        else:
            globals.ui.txt_mobile.setStyleSheet('background-color:#FFC0CB; color: black')
            globals.ui.txt_mobile.setText(None)
            globals.ui.txt_mobile.setPlaceholderText("Invalid phone")
            globals.ui.txt_mobile.setFocus()



    def capitalize(text, widget):
        try:
            capitalizedtext = str(text).title()
            widget.setText(capitalizedtext)

        except Exception as error:
            print("Error while capitalizing the name/surname ", error)