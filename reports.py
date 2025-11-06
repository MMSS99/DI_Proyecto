import datetime

from reportlab.pdfgen import canvas
import os

class Reports:

    def reportCustomers(self):
        try:
            data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            namereport = data + "_reportCostumers"

            c = canvas.Canvas('data/reports/customers.pdf')
            c.drawString(100, 100, "Customers")
            c.save()

            reportsPath = ".\\data\\reports\\"
            for file in os.listdir(reportsPath):
                if file.endswith(".pdf"):
                    os.startfile("%s/%s" % (reportsPath, file))

        except Exception as error:
            print("(!! Reports.reportCustomers) Error creating new report")