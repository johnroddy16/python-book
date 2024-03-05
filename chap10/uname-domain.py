# breaking down an email address:

address = 'johnroddy.16@yahoo.com'

uname, domain = address.split('@')

print('user name: %s, domain: %s' % (uname, domain))