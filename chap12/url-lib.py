# retrieving web pages with urllib library:

# with urllib we can treat a web page like a file and it will take care of all of the http protocol and header details for us:

import urllib.request

# read romeo.txt, like we did with socket in web-browse.py:   
 
# http://data.pr4e.org

word_kount = {}

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for a in fhand:
    # print(a.decode().strip())
    a = a.decode().lower().split()  # oh my goodness, i can do that?!
    # a = a.split()
    for w in a:
        word_kount[w] = word_kount.get(w, 0) + 1

print(word_kount)

fhand.close()

# headers are still sent but urllib consumes the header and only returns the relevant data