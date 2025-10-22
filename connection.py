import os
import sqlite3
import globals
from PyQt6 import QtSql, QtWidgets

class Connection:
    def db_connection(self = None):
        ruta_db = './data/bbdd.sqlite'

        if not os.path.isfile(ruta_db):
            QtWidgets.QMessageBox.critical(None, 'Error', 'El archivo de la base de datos no existe.',
                                           QtWidgets.QMessageBox.StandardButton.Cancel)
            return False
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(ruta_db)

        if db.open():
            query = QtSql.QSqlQuery()
            query.exec("SELECT name FROM sqlite_master WHERE type='table';")

            if not query.next():  # Si no hay tablas
                QtWidgets.QMessageBox.critical(None, 'Error', 'Base de datos vacía o no válida.',
                                               QtWidgets.QMessageBox.StandardButton.Cancel)
                return False
            else:
                QtWidgets.QMessageBox.information(None, 'Aviso', 'Conexión Base de Datos realizada',
                                                  QtWidgets.QMessageBox.StandardButton.Ok)
                return True
        else:
            QtWidgets.QMessageBox.critical(None, 'Error', 'No se pudo abrir la base de datos.',
                                           QtWidgets.QMessageBox.StandardButton.Cancel)
            return False

    def listProv(self=None):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM provincias;")
            list_prov = []

            if query.exec():
                while query.next():
                    list_prov.append(query.value(1))

                return list_prov

        except Exception as e:
            print("Error while fetching provinces form db ", e)

    @staticmethod
    def listMuniProv(province):
        try:
            list = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM municipios WHERE idprov = (SELECT idprov FROM provincias WHERE provincia = :province);")
            query.bindValue(":province", province)
            if query.exec():
                while query.next():
                    list.append(query.value(1))
                return list
        except Exception as e:
            print("Error while fetching municipalities form db ", e)

    @staticmethod
    def getCustomers():
        all_customers = []
        query = QtSql.QSqlQuery()
        query.prepare("SELECT * FROM customers WHERE historical = :false order by surname;")
        query.bindValue(":false", str(False))
        if query.exec():
            while query.next():
                row = [query.value(i) for i in range(query.record().count())]
                all_customers.append(row)
        return all_customers

    @staticmethod
    def getCustomerData(search_data, search_key):
        try:
            all_customer_data = []
            query = QtSql.QSqlQuery()
            match search_key:
                case "mobile":
                    query.prepare("SELECT * FROM customers WHERE mobile = :mobile;")
                    query.bindValue(":mobile", str(search_data).strip())
                case "ID":
                    query.prepare("SELECT * FROM customers WHERE dni_nie = :dni_nie;")
                    query.bindValue(":dni_nie", str(search_data).strip())

            if query.exec():
                while query.next():
                    for i in range(query.record().count()):
                        all_customer_data.append(query.value(i))

            return all_customer_data
        except Exception as error:
            print("Error getCustomerData: ", error)

    @staticmethod
    def deleteCustomer(dnicif):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE customers SET historical = :value WHERE dni_nie = :dnicif;")
            query.bindValue(":dnicif", dnicif)
            query.bindValue(":value", str(False))
            if query.exec():
                return True
            else:
                return False

        except Exception as error:
            print("Deleting connection method failed!", error)

    @staticmethod
    def addCustomer(customerInfo):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO customers VALUES (:dni_nie, :adddata, :surname, :name, :mail, :mobile, :address, :province, :city, :invoicetype, :historical);")

            valuePlaceholerList = [":dni_nie", ":adddata", ":surname", ":name", ":mail", ":mobile", ":address", ":province", ":city", ":invoicetype", ":historical"]
            for i in range(len(valuePlaceholerList)):
                query.bindValue(valuePlaceholerList[i], customerInfo[i])

            if query.exec():
                print ("(Connection.addCustomer) The next customer has been added: ", customerInfo)
                return True
            else:
                print("!!(Connection.addCustomer) Query execution has failed! ", customerInfo)
                return False


        except Exception as error:
            print("!!(Connection.addCustomer) Error saving the new customer! ", error)

    @staticmethod
    def alterCustomer(customerInfo):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE customers SET dni_nie = :dni_nie, adddata = :adddata, surname = :surname, name = :name, mail = :mail, mobile = :mobile, address = :address, province = :province, city = :city, invoicetype = :invoicetype, historical = :historical WHERE dni_nie = :dni_nie;")

            valuePlaceholerList = [":dni_nie", ":adddata", ":surname", ":name", ":mail", ":mobile", ":address", ":province", ":city", ":invoicetype", ":historical"]
            for i in range(len(valuePlaceholerList)):
                query.bindValue(valuePlaceholerList[i], customerInfo[i])

            if query.exec():
                print ("(Connection.alterCustomer) The next customer has been added: ", customerInfo)
                return True
            else:
                print("!!(Connection.alterCustomer) Query execution has failed! ", customerInfo)
                return False


        except Exception as error:
            print("!!(Connection.alterCustomer) Error saving the new customer! ", error)
