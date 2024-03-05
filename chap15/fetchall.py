# practicing with fetchall, sql:

import sqlite3

conn = sqlite3.connect('musik.sqlite')
c = conn.cursor()

c.execute('SELECT * FROM Tracks ORDER BY plays DESC')

x = c.fetchall()  # creates a list x of all the tuples selected, c.fetchall()[0] would choose the 0th tuple in list
print(x, type(x))

kount = 1

for i in x:
    if kount < 5:  # iterates over the list of tuples and displays the 0th and 1st elements in the tuples
        print('%d track: %s, plays: %d' % (kount, i[0], i[1]))
        kount += 1 

conn.close()