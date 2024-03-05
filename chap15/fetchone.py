# practicing with fetchone, sql:

import sqlite3

conn = sqlite3.connect('musik.sqlite')
c = conn.cursor()

# c.executescript('''
# INSERT INTO Tracks (title, plays) VALUES ('cant see me', 7);
# INSERT INTO Tracks (title, plays) VALUES ('sprinkle me', 8);
# INSERT INTO Tracks (title, plays) VALUES ('this is the way', 16);
# INSERT INTO Tracks (title, plays) VALUES ('california love', 24);
# INSERT INTO Tracks (title, plays) VALUES ('hurricane', 6);
# INSERT INTO Tracks (title, plays) VALUES ('dont worry be happy', 4)
# ''')

# conn.commit()

c.execute('SELECT * FROM Tracks')

x = c.fetchone()  # creates a tuple x from the first tuple in the selected data
print(x, type(x))

conn.close()