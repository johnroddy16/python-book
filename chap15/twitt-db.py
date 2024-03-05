# creating a datebase that can store the data retrieved from twspider.py from p4e book, chapter 15:

import sqlite3
import json 

conn = sqlite3.connect('twittdb.sqlite')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS Twitter (name TEXT, retrieved INTEGER, friends INTEGER)')

data = '''{
    "users" :
[
    { "id" : "001",
      "x" : "2",
      "screen_name" : "Chuck"
    },
    { "id" : "009",
      "x" : "8",
      "screen_name" : "Grant"
    }
]}'''


js = json.loads(data)
print(js, type(js))
print(json.dumps(js, indent=2))

for a in js['users']:
    friend = a['screen_name']
    print(friend)
    c.execute('INSERT INTO Twitter (name, retrieved, friends) VALUES (?, ?, ?)', (friend, 1, 1))

conn.commit()






conn.close()