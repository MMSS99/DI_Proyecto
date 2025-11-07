import datetime

from reportlab.pdfgen import canvas
import os

from connection import Connection


class Reports:

    def reportCustomers(self):
        try:
            data = datetime.datetime.now().strftime("%d_%m_%Y_%H-%M-%S")
            reportsPath = ".\\data\\reports\\"
            namereport = data + "_reportCostumers.pdf"
            pdf_path = os.path.join(reportsPath, namereport)

            records = Connection.getCustomers()
            c = canvas.Canvas(pdf_path)
            Reports.drawHeader(c)

            x = 55
            y = 625

            for record in records:
                if y >= 90:
                    Reports.drawClientInfo(c, record, y)
                    y -= 25
                else:
                    Reports.drawHeader(c)
                    y = 625

            #c.drawString(100, 100, "Customers")
            c.save()

            for file in os.listdir(reportsPath):
                if file.endswith(".pdf"):
                    os.startfile(pdf_path)

        except Exception as error:
            print("(!! Reports.reportCustomers) Error creating new report", error)

    @staticmethod
    def drawHeader(canvas):
        datafields = ["DNI_NIE", "SURNAME", "NAME", "PHONE", "CITY", "INVOICE", "STATUS"]
        datafieldsCardinality = [(55, 650), (110, 650), (210, 650), (280, 650), (335, 650), (440, 650), (490, 650)]
        canvas.setFont("Helvetica-Bold", 10)

        for i in range(len(datafields)):
            canvas.drawString(datafieldsCardinality[i][0], datafieldsCardinality[i][1], datafields[i])

        canvas.line(55, 640, 550, 640)

    @staticmethod
    def drawClientInfo(canvas, clientRecord, y):
        canvas.setFont("Helvetica", 8)
        dni = '***' + str(clientRecord[0])[4:7] + '***'
        values = [dni] + [str(clientRecord[i]) for i in range(len(clientRecord)) if i in (2, 3, 5, 8, 9)]
        cardinality = [(55, y), (110, y), (210, y), (280, y), (335, y), (440, y), (490, y)]

        for i in range(len(values)):
            canvas.drawString(cardinality[i][0], cardinality[i][1], values[i])

        if clientRecord[10]:
            canvas.drawString(cardinality[-1][0], cardinality[-1][1], "Active")
        else:
            canvas.drawString(cardinality[-1][0], cardinality[-1][1], "Inactive")



