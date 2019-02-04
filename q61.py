#coding:utf-8

text = '''title,author,year
The Weirdstone of Brisingamen, Alan Garner, 1960
Perdido Street Station, ChinaMiéville,2000 
Thud!, Terry Pratchett,2005 
The Spellman Files, Lisa Lutz,2007 
Small Gods, Terry Pratchett, 1992
'''

with open("many_books.csv", "wt") as outfile:
    outfile.write(text)
