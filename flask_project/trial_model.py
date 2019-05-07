import csv
import sqlite3
#
conn = sqlite3.connect('food.db')
c = conn.cursor()
c.execute("""create table swiggytable (name TEXT,price REAL)""")
c.execute("""create table zomatotable (name TEXT,price REAL)""")
c.execute("""create table ubereatstable (name TEXT,price REAL)""")
def database():
    with open('swiggy - Sheet1.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            c.execute("INSERT into swiggytable values (?,?)",(str(line[0]),float(line[1])))
    print("done")
def zomato_database():
    with open('zomato - Sheet1.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            c.execute("INSERT into zomatotable values (?,?)",(str(line[0]),float(line[1])))
    print("done")
def ubereats_database():
    with open('ubereats - Sheet1.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            c.execute("INSERT into ubereatstable values (?,?)",(str(line[0]),str(line[1])))
    print("done")

database()
zomato_database()
ubereats_database()

conn.commit()
conn.close()
