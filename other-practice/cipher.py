# practicing a cipher with .replace, this will be super basic for now:

alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

word = input('what is the word or message? ')

shift = int(input('what is the shift? '))

cipher_word = []

for a in word:
    a = a.lower()
    if a not in alphabet: 
        cipher_word.append(a)
        continue
    x = alphabet.find(a)
    y = alphabet[x + shift]
    cipher_word.append(y)

# print(cipher_word)

delim = ''

final_cipher = delim.join(cipher_word)
print(final_cipher)  # did not actually use .replace to do this but it is a nice little program