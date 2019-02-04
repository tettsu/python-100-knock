#coding:utf-8

import csv
import sqlite3
from q59 import db, cursor

ins_str = "insert into book values(?,?,?)"

with open("many_books.csv", "rt") as infile:
    books = csv.DictReader(infile)
    for book in books:
        cursor.execute(ins_str, (book["title"], book["author"], book["year"]))

db.commit