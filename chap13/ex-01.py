# exercise one from p4e book, chapter 13, using web services:

# edit geo-code.py to print out the two char country code from the retrieved data,
# add error checking so program will not trace back of the country code is not there:

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 'AIzaSyDSD2XIbfQ6mJT0dGaaF_Y8WMsrNoXaBoo'    # 42 

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

    try:
        c_c = js['results'][0]['address_components'][3]['short_name']  # country code 
    except:
        print('no country code found for %s' % address)
        continue

    print('the country code for the city you searched is %s' % c_c)