# parsing html using re:

# a simple web page:

# <h1>The First Page</h1>
# <p>
#     If you like, you can switch to the 
#     <a href="http://www.dr-chuck.com/page2.htm">
#         Second Page</a>
# </p>

# a re that will take on the form of a link on a html page:

r_e = 'href="http[s]?://.+?"'  # the ? means 0 or 1 and after + means non-greedy mode adn to find the smallest possible match

# search 4 link values within url input:

import urllib.request, urllib.parse, urllib.error
import re
import ssl

# ignore certificate erros:

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('enter url: ')
html = urllib.request.urlopen(url, context = ctx).read()
links = re.findall(b'href="(http[s]?://.+?)"', html)
for l in links:
    print(l.decode())

    