# more practice with strings:

ps1 = '    This / is a / good / string / 2 practice On    '

word = 'banana'

x = word.count('a')

print(x)
print()

# parsing strings:

data = 'From john.roddy.16@mit.edu.64 Sat May 20 09:14:26 2023'

atpos = data.find('@')

sppos = data.find(' ', atpos)

host = data[atpos + 1: sppos]

print(host)
print()