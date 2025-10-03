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
        query.prepare("SELECT * FROM customers order by surname;")
        if query.exec():
            while query.next():
                row = [query.value(i) for i in range(query.record().count())]
                all_customers.append(row)
        return all_customers