# atlantic ocean json from google geocode api:

# enter location: atlantic ocean
# retrieving https://maps.googleapis.com/maps/api/geocode/json?address=atlantic+ocean&key=AIzaSyDSD2XIbfQ6mJT0dGaaF_Y8WMsrNoXaBoo
# retrieved 1228 characters

import json 

atlantic = '''
{
  "results": [
    {
      "address_components": [
        {
          "long_name": "Atlantic Ocean",
          "short_name": "Atlantic Ocean",
          "types": [
            "establishment",
            "natural_feature"
          ]
        }
      ],
      "formatted_address": "Atlantic Ocean",
      "geometry": {
        "bounds": {
          "northeast": {
            "lat": 68.1962901,
            "lng": 19.9970779
          },
          "southwest": {
            "lat": -70.7734622,
            "lng": -82.9931606
          }
        },
        "location": {
          "lat": -14.5994134,
          "lng": -28.6731465
        },
        "location_type": "APPROXIMATE",
        "viewport": {
          "northeast": {
            "lat": 68.1962901,
            "lng": 19.9970779
          },
          "southwest": {
            "lat": -70.7734622,
            "lng": -82.9931606
          }
        }
      },
      "place_id": "ChIJ_7hu48qBWgYRT1MQ81ciNKY",
      "types": [
        "establishment",
        "natural_feature"
      ]
    }
  ],
  "status": "OK"
}'''
# lat: -14.599413, lng: -28.673147
# Atlantic Ocean

ocean = json.loads(atlantic)

print(json.dumps(ocean, indent = 2))