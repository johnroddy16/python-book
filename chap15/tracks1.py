# executing commands on musik.sqlite:

import sqlite3

conn = sqlite3.connect('musik.sqlite')
c = conn.cursor()

c.execute('DELETE FROM Tracks WHERE plays > 0')

c.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('picture me rollin', 8))
c.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('this is the end', 6))

conn.commit()  # we must commit!


c.execute('SELECT title, plays from Tracks')

for a in c:
    print(a)
    print(type(a))

conn.close()