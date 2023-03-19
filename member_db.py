import csv

class Member_DB:

    def __init__(self, header: list, mem: list):
        self.mem = mem
        self.header = ['name', 'email', 'password', 'phone number', 'status', 'level']

    def init_db(self, path):    #optional function (just to note the name of a column)
        path = path
        with open(path, 'w', encoding = 'UTF8') as a:
            writer = csv.writer(a)
            writer.writerow(self.header)
            a.close()

    def add_book(self, mem, path):
        mem = self.mem
        path = path
        with open(path, 'w', encoding = 'UTF8') as a:
            #open csv file
            writer = csv.writer(a)

            #write to the csv
            writer.writerow(mem)

            #close the csv
            a.close()

