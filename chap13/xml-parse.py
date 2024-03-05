# parsing XML:

import xml.etree.ElementTree as ET


xml = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes" />
</person>
'''

tree = ET.fromstring(xml)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
# print(dir(tree))
print()
# print(type(tree))