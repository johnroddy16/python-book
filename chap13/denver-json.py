# denver json from google geocode api:

# enter location: denver
# retrieving https://maps.googleapis.com/maps/api/geocode/json?address=denver&key=AIzaSyDSD2XIbfQ6mJT0dGaaF_Y8WMsrNoXaBoo
# retrieved 1739 characters

denver = {
  "results": [
    {
      "address_components": [
        {
          "long_name": "Denver",
          "short_name": "Denver",
          "types": [
            "locality",
            "political"
          ]
        },
        {
          "long_name": "Denver County",
          "short_name": "Denver County",
          "types": [
            "administrative_area_level_2",
            "political"
          ]
        },
        {
          "long_name": "Colorado",
          "short_name": "CO",
          "types": [
            "administrative_area_level_1",
            "political"
          ]
        },
        {
          "long_name": "United States",
          "short_name": "US",
          "types": [
            "country",
            "political"
          ]
        }
      ],
      "formatted_address": "Denver, CO, USA",
      "geometry": {
        "bounds": {
          "northeast": {
            "lat": 39.91424689999999,
            "lng": -104.6002959
          },
          "southwest": {
            "lat": 39.614431,
            "lng": -105.109927
          }
        },
        "location": {
          "lat": 39.7392358,
          "lng": -104.990251
        },
        "location_type": "APPROXIMATE",
        "viewport": {
          "northeast": {
            "lat": 39.91424689999999,
            "lng": -104.6002959
          },
          "southwest": {
            "lat": 39.614431,
            "lng": -105.109927
          }
        }
      },
      "place_id": "ChIJzxcfI6qAa4cR1jaKJ_j0jhE",
      "types": [
        "locality",
        "political"
      ]
    }
  ],
  "status": "OK"
}

# lat: 39.739236, lng: -104.990251
# Denver, CO, USA

print((denver['results'][0]['geometry']['location_type']))

x = 'short_name' in denver['results'][0]['address_components'][3]

y = denver['results'][0]['address_components'][3]['short_name']

print(x)

print(y)