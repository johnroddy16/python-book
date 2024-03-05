# looping thru nodes with XML:

import xml.etree.ElementTree as ET

data = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
'''

stuff = ET.fromstring(data)
lst = stuff.findall('users/user')  # findall creates a list with the elements being instances of user, we don't have to specify the outer
# print(lst)                       # tag <stuff>
print('user count %d' % len(lst))
print()
print(type(lst[0]))
print()

for u in lst:
    print('Name:', u.find('name').text)
    print('Id:', u.find('id').text)
    print('Attribute:', u.get('x'))