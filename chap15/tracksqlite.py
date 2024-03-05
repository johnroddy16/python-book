# db1.py from chapter 15 of p4e book:

import sqlite3

conn = sqlite3.connect('musik.sqlite')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS Tracks')
c.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
# c.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('picture me rollin', 4))

conn.close()