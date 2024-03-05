# practicing with the SELECT keyword in sqlite3:

import sqlite3

conn = sqlite3.connect('musik.sqlite')
c = conn.cursor()

c.execute('UPDATE Tracks SET plays = 18 WHERE title = "picture me rollin"')
conn.commit()

c.execute('SELECT title, plays FROM Tracks WHERE plays > 0 ORDER BY plays')

for a in c:
    print(a[0], a[1])


conn.close()