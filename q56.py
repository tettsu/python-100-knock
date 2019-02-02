text = '''author, book
JRR Tokien, The Hobbit
Lynne Truss, "Eats, Shoots & Leaves# '''

with open("books.csv", "wt") as outfile:
    outfile.write(text)

import csv
with open("books.csv", "rt") as infile:
    books = csv.DictReader(infile)
    for book in books:
        print(books)
        