# playing with a string:

words = 'there was a secret message sent and the key is the following: manhatten'

colon = words.rfind('p')  # will equal -1 if nothing found in the string

key = words[colon:]

print(key)