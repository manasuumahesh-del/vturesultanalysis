import os
from datetime import date
import csv


class File:

    def __init__(self, sem, reval, folderName):
        self.path = os.path.join(os.getcwd(), folderName)
        # Creating folder if not exists
        if not os.path.isdir(os.path.join(os.getcwd(), folderName)):
            os.makedirs(folderName)

        if not reval:
            self.name = f"reg-{sem}.csv"
        else:
            self.name = f"reval-{sem}.csv"

    def addData(self, data):
        # Manipulating data from db to insert
        try:
            if len(data) >= 1:
                usn = data[0][0]
                name = data[0][1]
                sem = data[0][2]
                announced = data[0][-2]
                data = [ele for row in data for ele in row[4:-1]]
                data.insert(0, usn)
                data.insert(1, name)
                data.insert(2, sem)
                # Adding announced date to file
                self.name = f"{str(date.today())}_{str(announced)}-{self.name}"
                with open(os.path.join(self.path, self.name), 'a', newline='') as csvfile:
                    csvwriter = csv.writer(csvfile).writerow(data)
        except Exception as e:
            print("Error occured while writing data!", e)
