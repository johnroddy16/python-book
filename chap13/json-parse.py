# parsong json:

import json

# must have double quotes:

data = '''
[
    { "id" : "001",
      "x" : "2",
      "name" : "Chuck"
    },
    { "id" : "009",
      "x" : "8",
      "name" : "Grant"
    }
]'''

info = json.loads(data)
# print(info)

print('user count: %d' % len(info))

print()

for a in info:
    print('name: %s' % a['name'])
    print('id: %s' % a['id'])
    print('attribute: %s' % a['x'])
    print()

print(info[0])