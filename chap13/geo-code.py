# google geocoding web service:

# a simple program that will prompt the user for a string, call the google geocoding api, and extract information from 
# the returned json:

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = '????????????????'    # 42  (ignore the number 42)

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'   # 'http://py4e-data.dr-chuck.net/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('enter location: ')
    if len(address) < 1: break

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
    print('lat: %.6f, lng: %.6f' % (lat, lng))
    location = js['results'][0]['formatted_address']
    print(location, type(location))
    city = location.split(',')
    print(city[0])
    print(len(js['results']))
    place_id = js['results'][0]['place_id']
    print(place_id, type(place_id))