# inspired by object and array format of javascript but since python is an older language than js the json syntax was
# influenced by the python syntax for dicts and lists:

import json

data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 418 206 9234"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

print(data)
print()
info = json.loads(data)
print(json.dumps(info, indent=2))
print()
x = json.dumps(info, indent=2)
print(x)

print()
print(info)
print()

print(len(info))

print(info['email']['hide'])