# a simpe program that will access the geocode api and store retrieved data in a database:
# before accessing the api it will check to see if the search has already been done for the particular location and if so ignore the
# request:


import urllib.request, urllib.parse, urllib.error
import json
import ssl
import sqlite3


api_key = '????????????????'    # 42 (ignore this) 

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'   # 'http://py4e-data.dr-chuck.net/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('geocodedb.sqlite')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS Location (name TEXT, lat REAL, lng REAL, placeid TEXT)')

while True:
    address = input('enter location: ')
    if len(address) < 1: break
    
    cap = address.capitalize()

    c.execute('SELECT * FROM Location WHERE name = (?)', (cap,))
    z = c.fetchone()

    if z != None:
        print('location already searched: %s' % address)
        continue 
     
    parms = {}
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('retrieving %s' % url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('retrieved %d characters' % len(data))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== faliure to retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent = 2))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    x = float('%.4f' % lat)
    y = float('%.4f' % lng)
    print('lat: %.6f, lng: %.6f' % (lat, lng))
    location = js['results'][0]['formatted_address']
    print(location, type(location))
    city = location.split(',')
    print(city[0])
    cit = city[0]
    print(len(js['results']))
    place_id = js['results'][0]['place_id']
    print(place_id, type(place_id))

    c.execute('SELECT * FROM Location WHERE name = (?)', (cit,))
    b = c.fetchone()

    if b != None:
        print('location already added to database: %s' % cit)
        continue 
        
    c.execute('INSERT INTO Location (name, lat, lng, placeid) VALUES (?, ?, ?, ?)', (cit, x, y, place_id))
    conn.commit()
    print('%s added to database with lat: %.4f, lng: %.4f, place id: %s' % (address, x, y, place_id))
    

conn.close()