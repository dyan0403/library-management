import csv

class Book_DB:

    def __init__(self, header: list, book: list):
        self.book = book
        self.header = ['title', 'author', 'book_id', 'subject', 'number_of_page', 'number_of_book']

    def init_db(self, path):    #optional function (just to note the name of a column)
        path = path
        with open(path, 'w', encoding = 'UTF8') as a:
            writer = csv.writer(a)
            writer.writerow(self.header)
            a.close()

    def add_book(self, book, path):
        book = self.book
        path = path
        with open(path, 'w', encoding = 'UTF8') as a:
            #open csv file
            writer = csv.writer(a)

            #write to the csv
            writer.writerow(book)

            #close the csv
            a.close()

