# practicing with select in sqlite3:

import sqlite3

conn = sqlite3.connect('musik.sqlite')
c = conn.cursor()

sing = 'picture me rollin'

c.execute('SELECT * FROM Tracks WHERE title = (?)', (sing,))

x = c.fetchone()  # returns none because no such title exists and the program runs fine
print(x)

if x != None:
    print(x[0])


conn.close()