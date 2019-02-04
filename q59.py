import sqlite3

db = sqlite3.connect("books.db")
cursor = db.cursor()
cursor.execute('''create table book (title, author, year)''')

db.commit