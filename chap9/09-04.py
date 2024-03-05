# advanced text parsing:

import string

print(string.punctuation)

word = 'baseball:!!/'

for a in word:
    if a in string.punctuation: continue
    print(a)


print(type(string.punctuation))  # class string